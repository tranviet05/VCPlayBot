import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = "BQApnomLhVuD6hOTzGOV-CFhJIOF7mYJYbWXLMpVZ9p16L1JtEfx1GPnkP3Z_A-ZOKS58TXQPEHlUgeluyNOCQ3xa0_kt83H3U_IFCNqLCwkx2PEL78Wkx9Iwwm8yHwVd_vfZk10hLi7283D3pe5eezSUGatASa25aD0Z127_-59Az4RqCAHIFn7DFZTv0M042YJueKGStKlTHyTnFJWH6Lx50CHADmPMdOO4D20TZeq72Deej1LUM1TMhOEJRltSNn4CPqJeerthDEG8BrwISwWqun-B6LTyh7edD32-6UA85RHCLRzQoQ0KqWtpa5pwylDcLHL5lBO3Y7zOCoDK5arbKJHRwA"
BOT_TOKEN = "5285501576:AAFq_V6osrcR3CvES8UJPlk-ri7nrtvmRdM"
BOT_NAME = "B-Airdrop Musical"
UPDATES_CHANNEL = "LaylaList"
BG_IMAGE = "https://telegra.ph/file/9b13ea3ce046a1a5c8098.png"
admins = {}
API_ID = "17721070"
API_HASH = "4bba50e58a9cdf2662fad1c8b6fb663c"
BOT_USERNAME = "b_airdropbot"
ASSISTANT_NAME = "VCPlayAssistant"
OWNER_NAME = "Taobaorich"
SUPPORT_GROUP = "AwesomeSupport"
PROJECT_NAME = "VCPlayBot2.0"
SOURCE_CODE = "github.com/tranviet05/VCPlayBot"
DURATION_LIMIT = "7"
ARQ_API_KEY = "BIOFMG-JYQCKM-RXMUYK-PBMIIS-ARQ"
PMPERMIT = "PMPERMIT"
LOG_GRP = "1001744882169"
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = "1822574407"
