"""Constants for the Octopus Germany integration."""

DOMAIN = "octopus_germany"

CONF_EMAIL = "email"
CONF_PASSWORD = "password"

# Update interval - 15 minutes is sufficient for price/meter data.
# Sebastian production fork: avoid 1-minute polling against the Octopus API.
UPDATE_INTERVAL = 15  # Update interval in minutes

# Schema exploration is useful while developing but too noisy for production HA.
EXPLORE_SCHEMA_ONCE = False

# Token management
TOKEN_REFRESH_MARGIN = (
    300  # Refresh token if less than 300 seconds (5 minutes) remaining
)
TOKEN_AUTO_REFRESH_INTERVAL = 50 * 60  # Auto refresh token every 50 minutes

# Debug options
DEBUG_ENABLED = False
LOG_API_RESPONSES = False  # Set to True to log full API responses
LOG_TOKEN_RESPONSES = (
    False  # Set to True to log token-related responses (login, refresh)
)
