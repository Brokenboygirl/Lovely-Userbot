from os import getenv

API_ID = int(getenv("API_ID", "9885470")) #optional
API_HASH = getenv("API_HASH", "84ff6bdb8eeb6e8bedf8a8192e3da3dd") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5440768701").split()))
OWNER_ID = int(getenv("OWNER_ID", "5440768701"))
MONGO_URL = getenv("MONGO_URL","mongodb+srv://AbishnoiMusic:AbishnoiMusic29@cluster0.k7sfn.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5811555216:AAEK_CxhnE8a50Pg_WkFEXwbLdi3WbrYGbQ")
ALIVE_PIC = getenv("ALIVE_PIC","https://te.legra.ph/file/cec5a117ff959166f7b6f.jpg")
ALIVE_TEXT = getenv("ALIVE_TEXT","NehalGupta")
PM_LOGGER = getenv("PM_LOGGER","")
LOG_GROUP = getenv("LOG_GROUP","-1001598879298")

STRING_SESSION1 = getenv("STRING_SESSION1", "BQCnUcB0lJj-s0Ba_yIylt88oUUTHk01jafThsULss2ACy6gq7v_SlM4xKz5yJNdcQQgpcpFq8v6hC_MJGBTxtIEup7Xerf3aF0Tto9jFxdvy4C6Rkjumb1w0xf2A4O800hz1XYDvhyEdRhnzCP5MmImRbrzvpieGJEJhGm48rYDjq-tAGooVIgB9EJ1vM0gJEtMEuCO-Wu4KPuOlvJE4LiKZXlkI1rE-XguM5RGnfjlFm_Ux1GSHqlJJLARlBB1Kq6c2B4kKNqJvPlKAbeOvXa8llAWx9v910vpWWJmOCDQAFyyWOuAjUMr2VgYA6ToYTjUdl2Tbtab3yGuehowDHbWAAAAAURLir0A")
STRING_SESSION2 = getenv("STRING_SESSION2", "AgC41oAbDTXABssO07zVPQafHn3oslVLrRdOkmKQ_LdJzpn5J2pC_1hnkCU-ICZQSAyBJtiOPznmGNgItYHzY_vbTA3suxF0P6D2CNyjhlKm3uEa5dx4jtaF_ZRPSAk4-OubXHL0mztqAa8gN7RLGxkthCn2hzFXxmzcRwIJOZPD6GOH7LtdG-oLbHK-1GMm0Mc_n6NoKSdQWKBO6n1jsbUQHWsV4AlPJHfyEiYdHEBTQll5xdV01_DvyZ3EDFXmNL0P4bdmqYcJvaQopgSaaiHiRrlhFvHUXgZoht3GfqGau2KB59pYXHE9IDzc4cB7HGikrCDdEredTD0GvgyzgawBAAAAAUC8D1sA")
STRING_SESSION3 = getenv("STRING_SESSION3", "BQAaxW6VWcOgbZWmNR5941pcfR9TPZ6C4OOVzzFapgiuAG_UqalnYSreu0gsoiIoIeVNJYkeGZZdoSbPYMSkUbppYkjs4_tSNw5tbds9xsSPnEljh7JM1LlbxPrCmKc6YPMnZ8VSIhrKJPyoUeWcgFKeUOSGEAQm6nFwUKPE6CFvOKs7E1a62biMj6rsmM0pQfE6Jl2AaUUgFHtFnTGiOPvERpH5DWydN4JdTySIru3IkU-ImanYsRz7ncO_PdCRYmVl5G87IY-wQ3NQVzolQsHySbb0hiHp3LkCuqhKsxCub4b8HvodEGGgq0AUinisFv358ANoiehO4hVPrszYuAY1AAAAAVN3_pUA")
STRING_SESSION4 = getenv("STRING_SESSION4", "AQCEYTC6WsRQlO-c0DWdT0tBRtyPbBF957PMIy1kuza6uNwHHInKWrSn1YFK_1efBWbOvsZUdkmYIGATrvR3IDbTMp35DwEAjRrlK8Re9ShKHa-usv3EC3HlrmhC_-VjSw6ra-6GNCIUHotExJHt9FkNUZT9rd-meUGi5KZT4zrJTVAOCYA8mCj0hM2DpXgkoIZ0agf2B4yKAFMlp7QrUvuzdtphxQ-OXi_Gr1kQF-yZTUQHcdBqAsr-0NuH6p6c63tglKO3Avz7S_-TF3Dfj8UaTt5vfCWeq7PDYu-sTDI2UXKiKGLw46ejW5ofyCYLqlE_98lHbxKJpJ7SWEmvspfbAAAAATerfzYA")
STRING_SESSION5 = getenv("STRING_SESSION5", "AQCyN2glOjlSH-MP8p2GY7oa6Uyj4cm8vHty8FpucfN9_LTw8H2fpboLouOzxHv-CIDNQBAwsqTruZ4Z6ZmTbRNbuif3I-0tWG4Ea_CYeLSCvpL0UOoAGK65Ug_zN8SpXYnafzUFDSEAMdVkthL_jWYYk18nijYYDzXqdJujbF4nvse0o36zDqzVS7ShwSQ0i4XoVeUChqcfRvkll_fdSXluvoJSmPo7u8ls-nXRA20oiXNERse5oMtC4eg4tZHHeiHkx6a8CHeY8Zf3liMXg5TW51X3Q3SczSWPf9YBO4gvOy5JugRdFzdNExImA-IpEZHHAUrwtg6P6dyCo_7enZruAAAAATiQa5sA")
STRING_SESSION6 = getenv("STRING_SESSION6", "BQBfXOu4lULQtX-WNl8MjE0oF2AiiCU0lbMjaT3Gl0k_Gx9jkx2aMNk_WHWp2ywnxcDNBqKR9u-mzifSWyDWCYcn_LKP9ilDMzwlxaA0Mp8o1vSGk-WBaiO-jKYB-3egmJl3cyzJsWWtfblAaMg7edP4asy6tnfd66IE6Yv0ivqxUIS47LZ5ePqPfpcttgWrXzmFs2e840EcshRGQi0dT-us7kJMhAVNiPGNIE4Y3U4BlGhsqJdAZmJ_2R6y9VqtuVSrHK73L3c-Of9ms-iWQ264zY8qZ3XcB11Zdzb-k_Y93DmAjKMZIjWMT7jTvyxtKvGk7Y2y-WQVE1UQZE7quT54AAAAAVSLsToA")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
