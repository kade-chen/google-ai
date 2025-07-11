from google import genai
from google.genai.types import Part,Content,  FileData, GenerateContentConfig, HttpOptions, ThinkingConfig
from google.oauth2 import service_account

MODEL = "gemini-2.0-flash-exp"

class GeminiBase:
    def __init__(self):
        service_account_key_path="/tmp/wdtest-001-bac69bfa6428.json"
        credentials = service_account.Credentials.from_service_account_file(
            service_account_key_path,
            scopes=['https://www.googleapis.com/auth/cloud-platform']
        )
        self.client = genai.Client(
            vertexai=True,
            credentials=credentials,
            project="wdtest-001",
            location="us-central1"
        )

    def generate_content_single(self, prompt):
        resp = self.client.models.generate_content_stream(
            # 流式输出
            model=MODEL,
            ## 支持多模态输入，eg: video + text
            contents=Content(
                parts=[Part(
                    file_data =  FileData(
                        file_uri="gs://lyon-bucket-central1/video/video_demo.mp4",
                        mime_type="video/mp4"
                    )
                ),
                    Part(
                        text=prompt,
                    )],
                role="user"
            ),
            config=GenerateContentConfig(
                temperature=0.9,
            ),
        )
        for chunk in resp:
            print(chunk.text)

if __name__ == '__main__':
    g = GeminiBase()
    g.generate_content_single("请你用中文描述我给你发的那个视频？")


