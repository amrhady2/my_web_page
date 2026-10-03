# Local configuration

This historical prototype requires external services and, in some cases, physical industrial hardware. Review the source before running it; some scripts write PLC tags, publish telemetry, or send messages.

Credentials are read from environment variables. Store Google service-account JSON outside this checkout and mount it read-only when using containers.

| Variable | Purpose |
| --- | --- |
| `GOOGLE_APPLICATION_CREDENTIALS` | Absolute path to your external Google service-account JSON |
| `SMTP_USER` | Email sender/login |
| `SMTP_PASSWORD` | Email application password |
| `SINCH_SERVICE_PLAN_ID` | SMS service-plan identifier |
| `SINCH_API_TOKEN` | SMS API token |
| `MQTT_PASSWORD` | MQTT broker password, where used |

Set only the variables used by the script you intend to run. Configure recipients and hardware endpoints for an authorized test environment. Never commit real credentials or notebook outputs containing credentials.
