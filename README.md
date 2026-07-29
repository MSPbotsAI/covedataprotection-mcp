# covedataprotection-mcp

MCP server for **Cove Data Protection** (N-able's backup/BDR platform,
formerly N-able Backup / Backup Manager). Exposes the Backup Manager
JSON-RPC **Management Service** API as MCP tools.

## Overview

- Stateless HTTP service. No credentials are ever persisted — each request
  supplies its own credentials via headers, used only for the lifetime of
  that single request.
- Supports concurrent requests; per-request credential isolation is done via
  Python `contextvars`, not a global/shared client instance.
- Entry points: `POST /mcp` (MCP protocol) and `GET /health` (health check).
- Default port: `8080` (configurable via `MCP_HTTP_PORT`).

## Scope

**247 tools**, one per JSON-RPC method in the official Management Service
schema (`Schema_23.3.json`, 251 methods total; 4 auth-only methods — `Login`,
`Authenticate`, `AuthenticateWithContext`, `GetAuthContextFromVisa` — are
handled internally by this server instead of exposed as tools). Per explicit
user decision, this covers the **full public API including write
operations** (Add/Remove/Modify/Set/Update, ~110 methods), not just the
71 `Get*` + 70 `Enumerate*` read methods. MSPbots itself only calls 6
report-style endpoints — see **Known Gaps** for the one MSPbots endpoint
this MCP does *not* cover.

## Authentication

Cove has no static long-lived API key. Instead, every session starts with a
**Login** call (`partner` + `username` + `password`) that returns a
short-lived **visa** token (valid ~15 minutes), which must accompany every
subsequent call.

This server does **not** cache a visa across requests — caching one would
mean persisting session state, which conflicts with the "no credential
persistence" requirement. Instead, `api_client.CoveClient.call()` performs a
fresh Login on *every* tool invocation and discards the resulting visa
afterward, trading one extra HTTP round trip per call for full statelessness.

### HEADER 授权参数说明

| Header | 类型 | 是否必填 | 默认值 | 枚举值 | 字段描述 | Example |
|---|---|---|---|---|---|---|
| `X-CoveDataProtection-Partner` | string | 是 | 无 | 无 | Login 的 `partner` 字段（登录所属的租户/合作伙伴名） | `Acme MSP (admin@example.com)` |
| `X-CoveDataProtection-Username` | string | 是 | 无 | 无 | Login 的 `username` 字段 | `mspbots` |
| `X-CoveDataProtection-Password` | string | 是 | 无 | 无 | Login 的 `password` 字段 | `••••••••` |

Missing any of the three headers returns `401`:
```json
{
  "error": "Missing credentials",
  "message": "This server requires the X-CoveDataProtection-Partner, X-CoveDataProtection-Username, and X-CoveDataProtection-Password headers",
  "required_headers": ["X-CoveDataProtection-Partner", "X-CoveDataProtection-Username", "X-CoveDataProtection-Password"],
  "optional_headers": []
}
```

## Environment Variables

| Variable | 类型 | 是否必填 | 默认值 | 说明 |
|---|---|---|---|---|
| `MCP_HTTP_PORT` | int | 否 | `8080` | HTTP 监听端口 |
| `MCP_HTTP_HOST` | string | 否 | `0.0.0.0` | HTTP 监听地址 |
| `COVEDATAPROTECTION_BASE_URL` | string | 否 | `https://api.backup.management/jsonapi` | Cove Management Service JSON-RPC 端点 |

## MCP Endpoint

- `POST /mcp` — MCP protocol (streamable HTTP transport)
- `GET /health` — health check, returns `{"status": "ok", "service": "covedataprotection-mcp", "transport": "http"}`

## Tool List

Tool names follow `covedataprotection_<snake_case_method_name>` — e.g. the
JSON-RPC method `EnumerateAccountStatistics` becomes
`covedataprotection_enumerate_account_statistics`. Parameter names mirror
the JSON-RPC method's own parameter names (camelCase → snake_case); complex
struct/enum-typed parameters are accepted as a `dict`/`str` and passed
through to the vendor API as-is — see **Known Gaps** for what that means in
practice.

| Category | Tool | JSON-RPC Method | 参数 |
|---|---|---|---|
| partners | `covedataprotection_add_partner` | AddPartner | partner_info(必填), create_default_account(必填) |
| partners | `covedataprotection_add_partner_ex` | AddPartnerEx | partner_info(必填), create_default_account(必填) |
| partners | `covedataprotection_change_partner_state` | ChangePartnerState | partner_id(必填), action(必填), reason(必填) |
| partners | `covedataprotection_enumerate_account_partner_id_tree` | EnumerateAccountPartnerIdTree | account_name(必填), account_password(必填) |
| partners | `covedataprotection_enumerate_advanced_partner_properties_infos` | EnumerateAdvancedPartnerPropertiesInfos | parent_partner_id(必填), fetch_recursively(必填) |
| partners | `covedataprotection_enumerate_advanced_partner_properties_infos_by_partner_ids` | EnumerateAdvancedPartnerPropertiesInfosByPartnerIds | partner_ids(必填) |
| partners | `covedataprotection_enumerate_ancestor_partners` | EnumerateAncestorPartners | partner_id(必填) |
| partners | `covedataprotection_enumerate_child_partners` | EnumerateChildPartners | partner_id(必填), fields(必填), partner_filter(必填), range(可选) |
| partners | `covedataprotection_enumerate_external_partner_properties` | EnumerateExternalPartnerProperties | partner_ids(必填) |
| partners | `covedataprotection_enumerate_partner_properties` | EnumeratePartnerProperties | 无 |
| partners | `covedataprotection_enumerate_partner_state_transitions` | EnumeratePartnerStateTransitions | 无 |
| partners | `covedataprotection_enumerate_partner_states_by_period` | EnumeratePartnerStatesByPeriod | start_time(必填), end_time(必填) |
| partners | `covedataprotection_enumerate_partner_urls` | EnumeratePartnerUrls | partner_id(必填) |
| partners | `covedataprotection_enumerate_partner_users_login_times` | EnumeratePartnerUsersLoginTimes | partner_ids(必填) |
| partners | `covedataprotection_enumerate_partners` | EnumeratePartners | parent_partner_id(必填), fetch_recursively(必填), fields(必填) |
| partners | `covedataprotection_enumerate_partners_at_time` | EnumeratePartnersAtTime | parent_partner_id(必填), fetch_recursively(必填), time(必填) |
| partners | `covedataprotection_enumerate_permitted_partners` | EnumeratePermittedPartners | entity(必填), action(必填), partner_ids(必填) |
| partners | `covedataprotection_enumerate_removed_partners` | EnumerateRemovedPartners | parent_partner_id(必填), start_time(必填), end_time(必填) |
| partners | `covedataprotection_enumerate_respect_removed_ancestor_partners_at_time` | EnumerateRespectRemovedAncestorPartnersAtTime | partner_id(必填), time(必填) |
| partners | `covedataprotection_enumerate_unique_partner_states_by_period` | EnumerateUniquePartnerStatesByPeriod | start_time(必填), end_time(必填) |
| partners | `covedataprotection_get_advanced_partner_properties` | GetAdvancedPartnerProperties | partner_id(必填) |
| partners | `covedataprotection_get_auto_deployment_partner_state` | GetAutoDeploymentPartnerState | partner_id(必填) |
| partners | `covedataprotection_get_partner_info` | GetPartnerInfo | name(必填) |
| partners | `covedataprotection_get_partner_info_at_time` | GetPartnerInfoAtTime | partner_id(必填), time(必填) |
| partners | `covedataprotection_get_partner_info_by_id` | GetPartnerInfoById | partner_id(必填) |
| partners | `covedataprotection_get_partner_info_by_uid` | GetPartnerInfoByUid | partner_uid(必填) |
| partners | `covedataprotection_get_partner_info_history` | GetPartnerInfoHistory | partner_id(必填), fields(必填) |
| partners | `covedataprotection_get_partner_price_currency` | GetPartnerPriceCurrency | partner_id(必填) |
| partners | `covedataprotection_get_partner_production_dates` | GetPartnerProductionDates | partner_id(必填) |
| partners | `covedataprotection_get_partner_state` | GetPartnerState | partner_id(必填) |
| partners | `covedataprotection_get_partner_tree` | GetPartnerTree | partner_id(必填), fields(必填), filter(必填), children_limit(必填), partner_filter(必填) |
| partners | `covedataprotection_get_partner_url` | GetPartnerUrl | partner_id(必填), url_type(必填) |
| partners | `covedataprotection_get_partner_users_login_times` | GetPartnerUsersLoginTimes | partner_id(必填) |
| partners | `covedataprotection_get_partners_rule_applied_to` | GetPartnersRuleAppliedTo | rule_id(必填) |
| partners | `covedataprotection_get_partners_rule_inactive_for` | GetPartnersRuleInactiveFor | rule_id(必填) |
| partners | `covedataprotection_get_root_partner_name` | GetRootPartnerName | 无 |
| partners | `covedataprotection_is_auto_deployment_allowed_for_partner` | IsAutoDeploymentAllowedForPartner | partner_id(必填) |
| partners | `covedataprotection_is_direct_debtor_partner` | IsDirectDebtorPartner | partner_id(必填) |
| partners | `covedataprotection_modify_auto_deployment_partner_state` | ModifyAutoDeploymentPartnerState | partner_id(必填), auto_deployment_state(必填) |
| partners | `covedataprotection_modify_partner` | ModifyPartner | partner_info(必填), force_remove_custom_column_values_in_old_scope(必填) |
| partners | `covedataprotection_regenerate_partner_uid` | RegeneratePartnerUid | partner_id(必填) |
| partners | `covedataprotection_register_external_partner_property` | RegisterExternalPartnerProperty | partner_property(必填) |
| partners | `covedataprotection_remove_partner` | RemovePartner | partner_id(必填) |
| partners | `covedataprotection_set_advanced_partner_properties` | SetAdvancedPartnerProperties | partner_id(必填), advanced_partner_properties_info(必填) |
| partners | `covedataprotection_set_partner_price_currency` | SetPartnerPriceCurrency | partner_id(必填), currency(必填) |
| partners | `covedataprotection_set_partner_url` | SetPartnerUrl | partner_id(必填), url_type(必填), url(必填) |
| accounts | `covedataprotection_add_account` | AddAccount | account_info(必填), home_node_info(必填) |
| accounts | `covedataprotection_add_account_node` | AddAccountNode | account_node_info(必填) |
| accounts | `covedataprotection_add_account_profile` | AddAccountProfile | account_profile_info(必填) |
| accounts | `covedataprotection_enumerate_account_nodes_by_account_token` | EnumerateAccountNodesByAccountToken | token(必填) |
| accounts | `covedataprotection_enumerate_account_profiles` | EnumerateAccountProfiles | partner_id(必填) |
| accounts | `covedataprotection_enumerate_account_statistics` | EnumerateAccountStatistics | query(必填) |
| accounts | `covedataprotection_enumerate_accounts` | EnumerateAccounts | partner_id(必填) |
| accounts | `covedataprotection_enumerate_ever_hosted_accounts` | EnumerateEverHostedAccounts | storage_node_id(必填) |
| accounts | `covedataprotection_enumerate_removed_accounts_by_ids` | EnumerateRemovedAccountsByIds | account_ids(必填) |
| accounts | `covedataprotection_get_account_features` | GetAccountFeatures | account_id(必填) |
| accounts | `covedataprotection_get_account_id` | GetAccountId | account_name(必填), account_password(必填) |
| accounts | `covedataprotection_get_account_info` | GetAccountInfo | name(必填), password(必填) |
| accounts | `covedataprotection_get_account_info_by_id` | GetAccountInfoById | account_id(必填) |
| accounts | `covedataprotection_get_account_info_by_id_with_removed` | GetAccountInfoByIdWithRemoved | account_id(必填) |
| accounts | `covedataprotection_get_account_info_by_token` | GetAccountInfoByToken | token(必填) |
| accounts | `covedataprotection_get_account_node_info` | GetAccountNodeInfo | account_node_id(必填) |
| accounts | `covedataprotection_get_account_node_info_by_guid` | GetAccountNodeInfoByGuid | node_guid(必填) |
| accounts | `covedataprotection_get_account_profile_info` | GetAccountProfileInfo | account_profile_id(必填) |
| accounts | `covedataprotection_modify_account` | ModifyAccount | account_info(必填), force_remove_custom_column_values_in_old_scope(必填) |
| accounts | `covedataprotection_modify_account_profile` | ModifyAccountProfile | account_profile_info(必填) |
| accounts | `covedataprotection_modify_accounts_batch` | ModifyAccountsBatch | account_ids(必填), account_info(必填) |
| accounts | `covedataprotection_relocate_account_node_by_token` | RelocateAccountNodeByToken | token(必填), from_storage_node_id(必填), to_storage_node_id(必填) |
| accounts | `covedataprotection_remove_account` | RemoveAccount | account_id(必填) |
| accounts | `covedataprotection_remove_account_data` | RemoveAccountData | account_id(必填) |
| accounts | `covedataprotection_remove_account_profile` | RemoveAccountProfile | account_profile_id(必填) |
| accounts | `covedataprotection_set_account_features` | SetAccountFeatures | account_id(必填), features(必填) |
| notifications | `covedataprotection_add_notification_rule` | AddNotificationRule | rule(必填) |
| notifications | `covedataprotection_add_notification_template` | AddNotificationTemplate | notification_template(必填) |
| notifications | `covedataprotection_add_notification_transport` | AddNotificationTransport | transport(必填) |
| notifications | `covedataprotection_enable_notification_rule` | EnableNotificationRule | rule_id(必填), partner_id(必填), enable(必填) |
| notifications | `covedataprotection_enumerate_all_active_notification_rules` | EnumerateAllActiveNotificationRules | 无 |
| notifications | `covedataprotection_enumerate_all_inactive_notification_rules` | EnumerateAllInactiveNotificationRules | 无 |
| notifications | `covedataprotection_enumerate_all_notification_rules` | EnumerateAllNotificationRules | 无 |
| notifications | `covedataprotection_enumerate_all_notification_transports` | EnumerateAllNotificationTransports | 无 |
| notifications | `covedataprotection_enumerate_notification_rules` | EnumerateNotificationRules | partner_id(必填) |
| notifications | `covedataprotection_enumerate_notification_transports` | EnumerateNotificationTransports | partner_id(必填) |
| notifications | `covedataprotection_enumerate_unsubscribed_emails` | EnumerateUnsubscribedEmails | entity(必填) |
| notifications | `covedataprotection_get_notification_rule` | GetNotificationRule | id(必填) |
| notifications | `covedataprotection_get_notification_template` | GetNotificationTemplate | id(必填) |
| notifications | `covedataprotection_get_notification_transport` | GetNotificationTransport | id(必填) |
| notifications | `covedataprotection_get_partner_notification_template` | GetPartnerNotificationTemplate | template_id(必填), partner_id(必填) |
| notifications | `covedataprotection_modify_notification_rule` | ModifyNotificationRule | rule(必填) |
| notifications | `covedataprotection_modify_notification_template` | ModifyNotificationTemplate | notification_template(必填) |
| notifications | `covedataprotection_modify_notification_transport` | ModifyNotificationTransport | transport(必填) |
| notifications | `covedataprotection_remove_notification_rule` | RemoveNotificationRule | id(必填) |
| notifications | `covedataprotection_remove_notification_template` | RemoveNotificationTemplate | id(必填) |
| notifications | `covedataprotection_remove_notification_transport` | RemoveNotificationTransport | id(必填) |
| notifications | `covedataprotection_unsubscribe_email_from_rule` | UnsubscribeEmailFromRule | token(必填) |
| notifications | `covedataprotection_unsubscribe_view_delivery` | UnsubscribeViewDelivery | token(必填) |
| users | `covedataprotection_add_user` | AddUser | user_info(必填) |
| users | `covedataprotection_add_user_settings` | AddUserSettings | user_settings(必填) |
| users | `covedataprotection_enumerate_user_roles` | EnumerateUserRoles | 无 |
| users | `covedataprotection_enumerate_user_settings` | EnumerateUserSettings | user_id(可选), settings_type(可选) |
| users | `covedataprotection_enumerate_users` | EnumerateUsers | partner_ids(必填) |
| users | `covedataprotection_enumerate_users_by_filter` | EnumerateUsersByFilter | filter(必填) |
| users | `covedataprotection_enumerate_users_with_security_officer_flag` | EnumerateUsersWithSecurityOfficerFlag | partner_id(必填) |
| users | `covedataprotection_get_respect_removed_user_info_by_id` | GetRespectRemovedUserInfoById | user_id(必填) |
| users | `covedataprotection_get_user_info` | GetUserInfo | partner_id(必填), name_or_email(必填), password(必填) |
| users | `covedataprotection_get_user_info_by_id` | GetUserInfoById | user_id(必填) |
| users | `covedataprotection_get_user_passport` | GetUserPassport | user_id(必填), authentication_context(必填) |
| users | `covedataprotection_get_user_settings` | GetUserSettings | settings_id(必填) |
| users | `covedataprotection_modify_user` | ModifyUser | user_info(必填) |
| users | `covedataprotection_modify_user_on_login` | ModifyUserOnLogin | user_info(必填) |
| users | `covedataprotection_modify_user_settings` | ModifyUserSettings | user_settings(必填) |
| users | `covedataprotection_remove_user` | RemoveUser | user_id(必填) |
| users | `covedataprotection_remove_user_settings` | RemoveUserSettings | settings_id(必填) |
| users | `covedataprotection_send_user_invitation` | SendUserInvitation | receiver_user_id(必填), redeem_link(必填), inviter_user_id(可选) |
| users | `covedataprotection_set_current_user_settings` | SetCurrentUserSettings | current_user_settings_info(必填) |
| misc | `covedataprotection_add_invitation_link` | AddInvitationLink | partner_id(必填), invitation_link(必填) |
| misc | `covedataprotection_enumerate_end_customer_prices` | EnumerateEndCustomerPrices | partner_id(必填) |
| misc | `covedataprotection_generate_reinstallation_passphrase` | GenerateReinstallationPassphrase | account_id(必填) |
| misc | `covedataprotection_get_auto_deploy_command_line` | GetAutoDeployCommandLine | partner_id(必填), profile_name(可选) |
| misc | `covedataprotection_get_auto_login_url` | GetAutoLoginUrl | partner_id(必填) |
| misc | `covedataprotection_get_common_statistics_by_token` | GetCommonStatisticsByToken | token(必填) |
| misc | `covedataprotection_get_effective_environment_info` | GetEffectiveEnvironmentInfo | 无 |
| misc | `covedataprotection_get_encryption_key_by_passphrase` | GetEncryptionKeyByPassphrase | account_id(必填), passphrase(必填) |
| misc | `covedataprotection_get_remote_client_connection_locator` | GetRemoteClientConnectionLocator | account_id(必填) |
| misc | `covedataprotection_get_server_info` | GetServerInfo | 无 |
| misc | `covedataprotection_is_sims_plugin_enabled` | IsSimsPluginEnabled | partner_id(必填) |
| misc | `covedataprotection_is_sims_plugin_enabled_for_any_child` | IsSimsPluginEnabledForAnyChild | partner_id(必填) |
| misc | `covedataprotection_lookup_transport` | LookupTransport | partner_id(必填), transport_type(必填) |
| misc | `covedataprotection_remove_personal_data` | RemovePersonalData | partner_id(必填), from_timestamp(可选), to_timestamp(可选) |
| misc | `covedataprotection_set_end_customer_price` | SetEndCustomerPrice | partner_id(必填), end_customer_price(必填) |
| misc | `covedataprotection_update_statistics` | UpdateStatistics | posting(必填) |
| misc | `covedataprotection_verify_encryption_key` | VerifyEncryptionKey | account_id(必填), encryption_key(必填) |
| storage_nodes | `covedataprotection_add_storage_node` | AddStorageNode | storage_node_info(必填) |
| storage_nodes | `covedataprotection_enumerate_all_storage_nodes` | EnumerateAllStorageNodes | 无 |
| storage_nodes | `covedataprotection_enumerate_storage_nodes` | EnumerateStorageNodes | storage_id(必填) |
| storage_nodes | `covedataprotection_enumerate_storage_nodes_by_account_id` | EnumerateStorageNodesByAccountId | accounts(必填) |
| storage_nodes | `covedataprotection_enumerate_storage_nodes_with_environments` | EnumerateStorageNodesWithEnvironments | storage_id(必填) |
| storage_nodes | `covedataprotection_get_storage_node_info` | GetStorageNodeInfo | storage_node_id(必填) |
| storage_nodes | `covedataprotection_get_storage_node_info_by_name` | GetStorageNodeInfoByName | storage_id(必填), name(必填) |
| storage_nodes | `covedataprotection_get_storage_node_update_info` | GetStorageNodeUpdateInfo | partner_id(必填) |
| storage_nodes | `covedataprotection_remove_storage_node` | RemoveStorageNode | storage_node_id(必填) |
| storage_nodes | `covedataprotection_report_storage_node_environment` | ReportStorageNodeEnvironment | storage_node_environment_info(必填) |
| storage_nodes | `covedataprotection_resolve_storage_node_executor` | ResolveStorageNodeExecutor | partner_name(必填), storage_name(必填), storage_node_name(必填) |
| storage_nodes | `covedataprotection_update_storage_node` | UpdateStorageNode | storage_node_id(必填), update_with(必填) |
| storage_nodes | `covedataprotection_update_storage_node_mode` | UpdateStorageNodeMode | storage_node_id(必填), storage_node_mode_info(必填) |
| storage_nodes | `covedataprotection_update_storage_node_state` | UpdateStorageNodeState | storage_node_id(必填), storage_node_state_info(必填) |
| contacts | `covedataprotection_add_contact_note` | AddContactNote | contact_note_info(必填) |
| contacts | `covedataprotection_add_contact_person` | AddContactPerson | contact_person_info(必填) |
| contacts | `covedataprotection_enumerate_all_contact_persons` | EnumerateAllContactPersons | root_partner_id(必填), contact_person_types(必填), apply_mailing_option(必填) |
| contacts | `covedataprotection_enumerate_contact_notes` | EnumerateContactNotes | partner_id(必填) |
| contacts | `covedataprotection_enumerate_contact_persons` | EnumerateContactPersons | partner_ids(必填) |
| contacts | `covedataprotection_enumerate_last_contact_notes` | EnumerateLastContactNotes | partners(必填) |
| contacts | `covedataprotection_get_contact_note_info` | GetContactNoteInfo | contact_note_id(必填) |
| contacts | `covedataprotection_get_contact_person_info_by_id` | GetContactPersonInfoById | contact_person_id(必填) |
| contacts | `covedataprotection_modify_contact_note` | ModifyContactNote | contact_note_info(必填) |
| contacts | `covedataprotection_modify_contact_person` | ModifyContactPerson | contact_person_info(必填) |
| contacts | `covedataprotection_remove_contact_note` | RemoveContactNote | contact_note_id(必填) |
| contacts | `covedataprotection_remove_contact_person` | RemoveContactPerson | contact_person_id(必填) |
| storage | `covedataprotection_add_storage` | AddStorage | add_storage_info(必填) |
| storage | `covedataprotection_enumerate_software_only_ancestral_partners_storages` | EnumerateSoftwareOnlyAncestralPartnersStorages | partner_id(必填) |
| storage | `covedataprotection_enumerate_storage_statistics` | EnumerateStorageStatistics | partner_id(必填) |
| storage | `covedataprotection_enumerate_storages` | EnumerateStorages | partner_id(必填) |
| storage | `covedataprotection_get_reserved_storage` | GetReservedStorage | storage_node_id(必填) |
| storage | `covedataprotection_get_storage_info` | GetStorageInfo | storage_id(必填) |
| storage | `covedataprotection_get_storage_info_by_name` | GetStorageInfoByName | partner_id(必填), name(必填) |
| storage | `covedataprotection_modify_storage` | ModifyStorage | storage_id(必填), storage_info(必填) |
| storage | `covedataprotection_remove_storage` | RemoveStorage | storage_id(必填) |
| storage | `covedataprotection_reserve_storage_on_account_node` | ReserveStorageOnAccountNode | node_guid(必填), reserved_size(必填) |
| view_delivery | `covedataprotection_add_view_delivery` | AddViewDelivery | view_delivery_info(必填) |
| view_delivery | `covedataprotection_enumerate_view_deliveries` | EnumerateViewDeliveries | user_id(必填) |
| view_delivery | `covedataprotection_get_view_delivery_external_recipients_states` | GetViewDeliveryExternalRecipientsStates | view_delivery_id(必填) |
| view_delivery | `covedataprotection_get_view_delivery_info_by_id` | GetViewDeliveryInfoById | view_delivery_id(必填) |
| view_delivery | `covedataprotection_get_view_delivery_recipients_states` | GetViewDeliveryRecipientsStates | view_delivery_id(必填) |
| view_delivery | `covedataprotection_is_view_delivery_enabled` | IsViewDeliveryEnabled | partner_id(必填) |
| view_delivery | `covedataprotection_modify_view_delivery` | ModifyViewDelivery | view_delivery_info(必填) |
| view_delivery | `covedataprotection_opt_in_view_delivery` | OptInViewDelivery | token(必填) |
| view_delivery | `covedataprotection_perform_view_delivery` | PerformViewDelivery | view_delivery_id(必填) |
| view_delivery | `covedataprotection_remove_view_delivery` | RemoveViewDelivery | view_delivery_id(必填) |
| labels | `covedataprotection_add_account_label` | AddAccountLabel | account_id_collection(必填), label_collection(必填) |
| labels | `covedataprotection_add_labels` | AddLabels | account_id(必填), label_collection(必填) |
| labels | `covedataprotection_enumerate_account_ids_by_label` | EnumerateAccountIdsByLabel | label(必填) |
| labels | `covedataprotection_enumerate_account_labels_by_account_id` | EnumerateAccountLabelsByAccountId | account_id(必填) |
| labels | `covedataprotection_enumerate_account_labels_by_account_ids` | EnumerateAccountLabelsByAccountIds | account_ids(必填) |
| labels | `covedataprotection_enumerate_account_labels_by_names` | EnumerateAccountLabelsByNames | label_collection(必填) |
| labels | `covedataprotection_enumerate_all_labels` | EnumerateAllLabels | 无 |
| labels | `covedataprotection_remove_account_label` | RemoveAccountLabel | account_id_collection(必填), label_collection(必填) |
| labels | `covedataprotection_remove_labels` | RemoveLabels | account_id(必填), label_collection(必填) |
| jobs | `covedataprotection_add_root_job` | AddRootJob | partner_id(必填), specification(必填), executor_id(必填) |
| jobs | `covedataprotection_control_job` | ControlJob | job_id(必填), action(必填) |
| jobs | `covedataprotection_enumerate_jobs` | EnumerateJobs | partner_id(必填) |
| jobs | `covedataprotection_enumerate_jobs_by_ids` | EnumerateJobsByIds | ids(必填) |
| jobs | `covedataprotection_enumerate_jobs_by_parent_id` | EnumerateJobsByParentId | parent_job_id(必填), fetch_recursively(必填) |
| jobs | `covedataprotection_finish_job_execution` | FinishJobExecution | job_id(必填), execution_info(必填) |
| jobs | `covedataprotection_get_job_by_id` | GetJobById | job_id(必填) |
| jobs | `covedataprotection_report_job_execution_progress` | ReportJobExecutionProgress | job_id(必填), execution_info(必填) |
| jobs | `covedataprotection_take_job_for_execution` | TakeJobForExecution | executor_type(必填), executor_id(必填) |
| custom_columns | `covedataprotection_add_custom_column` | AddCustomColumn | custom_column(必填) |
| custom_columns | `covedataprotection_enumerate_columns` | EnumerateColumns | partner_id(必填) |
| custom_columns | `covedataprotection_enumerate_custom_columns` | EnumerateCustomColumns | partner_id(必填) |
| custom_columns | `covedataprotection_get_account_custom_column_values` | GetAccountCustomColumnValues | account_id(必填) |
| custom_columns | `covedataprotection_get_custom_column_info_by_id` | GetCustomColumnInfoById | custom_column_id(必填) |
| custom_columns | `covedataprotection_modify_custom_column` | ModifyCustomColumn | custom_column(必填) |
| custom_columns | `covedataprotection_remove_custom_column` | RemoveCustomColumn | custom_column_id(必填) |
| custom_columns | `covedataprotection_update_account_custom_column_values` | UpdateAccountCustomColumnValues | account_id(必填), values(必填) |
| branding | `covedataprotection_find_branding` | FindBranding | partner_id(必填), application_type(必填) |
| branding | `covedataprotection_get_effective_partner_branding` | GetEffectivePartnerBranding | application_type(必填) |
| branding | `covedataprotection_get_partner_branding` | GetPartnerBranding | partner_id(必填) |
| branding | `covedataprotection_get_partner_web_branding` | GetPartnerWebBranding | partner_id(必填) |
| branding | `covedataprotection_reset_branding` | ResetBranding | partner_id(必填), application_type(必填) |
| branding | `covedataprotection_set_branding` | SetBranding | partner_id(必填), application_type(必填), branding_body(必填) |
| branding | `covedataprotection_set_partner_branding` | SetPartnerBranding | partner_id(必填), branding_archive(必填) |
| branding | `covedataprotection_set_partner_web_branding` | SetPartnerWebBranding | partner_id(必填), web_branding_archive(必填) |
| products | `covedataprotection_add_product` | AddProduct | product_info(必填) |
| products | `covedataprotection_enumerate_products` | EnumerateProducts | partner_id(必填), current_partner_only(必填) |
| products | `covedataprotection_find_product_by_name` | FindProductByName | partner_id(必填), name(必填) |
| products | `covedataprotection_get_product_info` | GetProductInfo | product_id(必填), return_modified_features_only(必填) |
| products | `covedataprotection_get_product_info_with_extra_features` | GetProductInfoWithExtraFeatures | product_id(必填), return_modified_features_only(必填) |
| products | `covedataprotection_modify_product` | ModifyProduct | product_info(必填) |
| products | `covedataprotection_remove_product` | RemoveProduct | product_id(必填) |
| eula | `covedataprotection_accept_eula` | AcceptEula | full_name(必填), role(必填) |
| eula | `covedataprotection_decline_eula` | DeclineEula | full_name(必填), role(必填) |
| eula | `covedataprotection_get_common_eula_info` | GetCommonEulaInfo | 无 |
| eula | `covedataprotection_get_end_customer_eula_state` | GetEndCustomerEulaState | user_id(必填) |
| eula | `covedataprotection_get_eula_info` | GetEulaInfo | 无 |
| eula | `covedataprotection_get_partner_eula_info` | GetPartnerEulaInfo | partner_id(必填) |
| locations | `covedataprotection_add_location` | AddLocation | location_info(必填) |
| locations | `covedataprotection_enumerate_locations` | EnumerateLocations | 无 |
| locations | `covedataprotection_get_location_info` | GetLocationInfo | location_id(必填) |
| locations | `covedataprotection_get_location_info_by_name` | GetLocationInfoByName | location_name(必填) |
| locations | `covedataprotection_return_account_to_home_location` | ReturnAccountToHomeLocation | account_id(必填) |
| countries | `covedataprotection_enumerate_account_remote_access_endpoints` | EnumerateAccountRemoteAccessEndpoints | account_id(必填) |
| countries | `covedataprotection_enumerate_countries` | EnumerateCountries | 无 |
| countries | `covedataprotection_get_country_by_iso_code` | GetCountryByIsoCode | country_iso_code(必填) |
| countries | `covedataprotection_get_country_by_iso_code_or_name` | GetCountryByIsoCodeOrName | country_iso_code_or_name(必填) |
| countries | `covedataprotection_get_country_by_name` | GetCountryByName | country_name(必填) |
| audit | `covedataprotection_enumerate_audit_action_entity_types` | EnumerateAuditActionEntityTypes | 无 |
| audit | `covedataprotection_enumerate_audit_action_operation_types` | EnumerateAuditActionOperationTypes | 无 |
| audit | `covedataprotection_enumerate_audit_action_result_types` | EnumerateAuditActionResultTypes | 无 |
| audit | `covedataprotection_enumerate_audit_actions` | EnumerateAuditActions | action_info(必填), from_(必填), to(必填), count_limit(必填), include_all_sub_partners(必填), reverse_order(必填) |
| email | `covedataprotection_get_amazon_endpoint_for_email` | GetAmazonEndpointForEmail | email(必填) |
| email | `covedataprotection_register_email` | RegisterEmail | email(必填) |
| email | `covedataprotection_unregister_email` | UnregisterEmail | email(必填) |
| regions | `covedataprotection_add_region` | AddRegion | region_info(必填) |
| regions | `covedataprotection_enumerate_regions` | EnumerateRegions | 无 |
| features | `covedataprotection_enumerate_features` | EnumerateFeatures | partner_id(必填) |
| features | `covedataprotection_reset_features_restrictions` | ResetFeaturesRestrictions | partner_id(必填) |
| permissions | `covedataprotection_enumerate_permissions` | EnumeratePermissions | 无 |
| templates | `covedataprotection_enumerate_templates` | EnumerateTemplates | partner_id(必填), partner_only(必填) |

## 测试示例

```bash
# Health check
curl -s http://localhost:8080/health

# Call a tool via the MCP protocol (streamable HTTP) — requires an
# initialize handshake first per the MCP spec; abbreviated example below
# shows the tool-call request body only:
curl -s -X POST http://localhost:8080/mcp \
  -H "X-CoveDataProtection-Partner: <your-partner-name>" \
  -H "X-CoveDataProtection-Username: <your-username>" \
  -H "X-CoveDataProtection-Password: <your-password>" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "mcp-session-id: <session-id-from-initialize>" \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/call",
    "params": {
      "name": "covedataprotection_get_server_info",
      "arguments": {}
    }
  }'
```

Expected: `200` with the server version on valid credentials; on invalid
credentials, the `Login` call itself fails and every tool surfaces
`Error: Cove Data Protection API error ...` with the vendor's JSON-RPC error
message.

**Live-verified** (2026-07-29): `covedataprotection_get_server_info` (zero
parameters) was called end-to-end through this running server with a real
partner/username/password and returned the actual Cove server version —
confirming the Login → visa → method-call pipeline works against the live
API, not just structurally.

## API Reference

- Getting Started: https://developer.n-able.com/n-able-cove/docs/getting-started
- Authorization: https://developer.n-able.com/n-able-cove/docs/authorization
- Constructing a call: https://developer.n-able.com/n-able-cove/docs/construct-a-json-rpc-api-call
- Full method/struct/enum schema (JSON): https://documentation.n-able.com/covedataprotection/Schema_23.3.json

## Known Gaps

- **This covers the Management Service only.** Cove's Getting Started guide
  describes a second, separate **Reporting Service** (`{host}/repserv_json`,
  runs per storage node) that provides backup/restore session statistics.
  MSPbots' own configuration calls a "Query Sessions" report against this
  Reporting Service — it is **not** part of the 251-method Management
  Service schema this MCP is generated from, and no public schema for the
  Reporting Service was found. This is the one MSPbots-configured endpoint
  this MCP does not cover; it can be added if the Reporting Service's
  method list/schema becomes available.
- **Complex struct/enum parameters are untyped (`dict`/`str`) rather than
  fully modeled.** The schema defines 106 structs and 78 enums; fully
  reproducing each one as a typed Python parameter was out of scope for a
  247-tool mechanical generation. Callers need to shape these dict
  arguments to match the vendor's schema (see the Structs section of
  `Schema_23.3.json` for exact field names) — the tool docstrings name the
  original JSON-RPC parameter name and type to help with this.
- **No visa caching** — see the Authentication section above. Every tool
  call performs its own Login, which is simple and fully stateless but
  means 2 HTTP requests to the vendor per tool call instead of 1.
- All 247 tools were code-generated directly from the vendor's own schema
  file, not hand-written — parameter names/types are only as accurate as
  that schema. `covedataprotection_get_server_info` was the one tool
  live-verified end-to-end; the rest are structurally correct (schema
  validated, MCP-protocol tools/list confirmed) but not individually
  smoke-tested against real data.
