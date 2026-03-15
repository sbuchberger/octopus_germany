"""Constants for the Octopus Germany integration."""

DOMAIN = "octopus_germany"

CONF_EMAIL = "email"
CONF_PASSWORD = "password"

# Update interval - 15 minutes is sufficient for price/meter data
UPDATE_INTERVAL = 15  # Update interval in minutes

# Schema exploration (run once for debugging)
EXPLORE_SCHEMA_ONCE = False  # Disabled for production use

# Token management
TOKEN_REFRESH_MARGIN = (
    300  # Refresh token if less than 300 seconds (5 minutes) remaining
)
TOKEN_AUTO_REFRESH_INTERVAL = 50 * 60  # Auto refresh token every 50 minutes

# Debug options
DEBUG_ENABLED = False  # Disabled for production use
LOG_API_RESPONSES = False
LOG_TOKEN_RESPONSES = False
