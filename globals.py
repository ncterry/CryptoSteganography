# This is our global list.
# While the program is running this will be used with our study data
global global_photoName
global_photoName = "fox_original.jpg"

global globalMain_Directory
globalMain_Directory = "/Users/nct/Dropbox/ComputerScience/PycharmProjects/CryptoSteganography"

# Set photo directory address in StudyPage, so the PhotoPage knows what to open
# We set it to a stock photo initially, so the PhotoPage can open up front.
global globalOriginalPhoto_Directory
globalOriginalPhoto_Directory = "/Users/nct/Dropbox/ComputerScience/PycharmProjects/CryptoSteganography/CryptoSteganography/OriginalPhotos/"

# Set the photo directory for encrypted photos
global globalEncryptedPhoto_Directory
globalEncryptedPhoto_Directory = "/Users/nct/Dropbox/ComputerScience/PycharmProjects/CryptoSteganography/CryptoSteganography/StegoPhotos/"

global unsecuredMessage
unsecuredMessage = ""

global workingPXLs
workingPXLs = 0

global joinJoinJoin
joinJoinJoin = ""


# =========for the AES encryption ====start=======
global key
key = b'Sixteen byte key' # he made this global

global message
message = "this is my super secret message"

from Crypto.Cipher import AES
global cipher
cipher = AES.new(key)
# =========for the AES encryption ====end=======
