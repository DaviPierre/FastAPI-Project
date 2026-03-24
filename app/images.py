from dotenv import load_dotenv
from imagekitio import ImageKit
import os
from typing import TypedDict, List, Optional

load_dotenv()

imagekit = ImageKit(
    private_key=os.getenv("IMAGEKIT_PRIVATE_KEY"),
)

imagekit_public_key = os.getenv("IMAGEKIT_PUBLIC_KEY")

url_endpoint = os.getenv("IMAGEKIT_URL")

class UploadFileRequestOptions(TypedDict, total=False):
    use_unique_file_name: bool
    folder: str
    tags: List[str]


