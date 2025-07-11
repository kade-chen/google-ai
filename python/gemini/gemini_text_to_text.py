import tracemalloc
from google import genai
from google.genai.types import Part,Content, GenerateContentConfig, HttpOptions
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
            contents=Content(
                parts=[Part(
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
    g.generate_content_single("介绍一下你能做些什么")


