from configs import LND_HOST, LND_MACAROON, LND_CERTIFICATE
from lnd import Lnd

lnd = Lnd(LND_HOST, LND_MACAROON, LND_CERTIFICATE)