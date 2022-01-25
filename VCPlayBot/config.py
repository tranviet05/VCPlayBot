import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("BQApnomLhVuD6hOTzGOV-CFhJIOF7mYJYbWXLMpVZ9p16L1JtEfx1GPnkP3Z_A-ZOKS58TXQPEHlUgeluyNOCQ3xa0_kt83H3U_IFCNqLCwkx2PEL78Wkx9Iwwm8yHwVd_vfZk10hLi7283D3pe5eezSUGatASa25aD0Z127_-59Az4RqCAHIFn7DFZTv0M042YJueKGStKlTHyTnFJWH6Lx50CHADmPMdOO4D20TZeq72Deej1LUM1TMhOEJRltSNn4CPqJeerthDEG8BrwISwWqun-B6LTyh7edD32-6UA85RHCLRzQoQ0KqWtpa5pwylDcLHL5lBO3Y7zOCoDK5arbKJHRwA", "session")
BOT_TOKEN = getenv("5285501576:AAFq_V6osrcR3CvES8UJPlk-ri7nrtvmRdM")
BOT_NAME = getenv("B-Airdrop Musical")
UPDATES_CHANNEL = getenv("LaylaList")
BG_IMAGE = getenv("https://telegra.ph/file/9b13ea3ce046a1a5c8098.png")
admins = {}
API_ID = int(getenv("17721070"))
API_HASH = getenv("4bba50e58a9cdf2662fad1c8b6fb663c")
BOT_USERNAME = getenv("b_airdropbot")
ASSISTANT_NAME = getenv("VCPlayAssistant")
OWNER_NAME = getenv("Taobaorich")
SUPPORT_GROUP = getenv("AwesomeSupport")
PROJECT_NAME = getenv("VCPlayBot2.0")
SOURCE_CODE = getenv("github.com/tranviet05/VCPlayBot")
DURATION_LIMIT = int(getenv("7"))
ARQ_API_KEY = getenv("BIOFMG-JYQCKM-RXMUYK-PBMIIS-ARQ", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("1001744882169", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("1822574407").split()))
