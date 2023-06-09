import os

from jdx_utils.api.secrets import get_secret_from_sm

shopify_secret_name = {
    'dev': 'dsb-shopify-dev2-secret',
    'beta': 'dsb-shopify-beta-secrets',
    'prd': 'dsb-shopify-app-token'
}

SHOPIFY_SECRET_NAME = shopify_secret_name[os.environ['ENV']]

# product details
FST_PRODUCT_ID='7788774621433'
FST_SKU = '50875e49-4485-4405-b329-69877c13ee2d'
FST_BARCODE = '196852085453'
FST_LP = 89.00

NIPS_BASIC_SKU = '2adc5ddf-e519-480c-966d-1385c8592d81'
NIPS_BASIC_BARCODE = '197644902637'
NIPS_BASIC_LP = 599.00

NIPS_PLUS_SKU = '98e2f68b-1b55-48df-b9d3-8953bf926b7d'
NIPS_PLUS_BARCODE = '197644105045'
NIPS_PLUS_LP = 699.00


# Get Snowflake credentials
SNOWFLAKE_SECRET_NAME = 'dsb-snowflake-secrets'
SNOWFLAKE_WH = 'DSB_ANALYTICS_WH'

# Jotform details
JOTFORM_SECRET_NAME = 'dsb-jotform-api-key'
JOTFORM_ID_REDRAW ='231075275142955'
JOTFORM_ID_HAZEL = '231069003892959'
JOTFORM_ID_BIRCH = '231068067067962'

# Google Sheet
GOOGLE_API_SECRET_NAME = 'dsb-ingestion-bot-key'
INVENTORY_SHEET_ID = '1-TTSt61uvWsVNI93boGyijqAWVcwzd_B4MfSA6u4_sA'
ORDER_CREATION_SHEET_ID = '1pP7oib65GRye7VXOt06xO5S17oA9tP0ixDP2Jt43q_o'
AMAZON_FBA_USER_SHEET_ID = '1JgoRadxvhUM9beOO4voGpPpucfX8SHT7ettjBShB9-4'

# Slack
slack_secret_mapping = {
    'dev': 'dsb-slack-api-token-test',
    'prd': 'dsb-slack-api-token'
}

SLACK_BOT_SECRET_NAME = slack_secret_mapping[os.environ['ENV']]

# Get slack secrets
slack_secrets = get_secret_from_sm(SLACK_BOT_SECRET_NAME)
SLACK_BOT_TOKEN = slack_secrets['SLACK_BOT_TOKEN']
SLACK_APP_TOKEN = slack_secrets['SLACK_APP_TOKEN']