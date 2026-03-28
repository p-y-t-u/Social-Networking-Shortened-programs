from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

def main():
    try:
        creds = InstalledAppFlow.from_client_secrets_file(
            'credentials.json',
            ['https://www.googleapis.com/auth/drive.metadata.readonly']
        ).run_local_server(port=0)

        items = build('drive', 'v3', credentials=creds)\
            .files().list(pageSize=10).execute().get('files', [])

        print("Files in your Google Drive:\n" if items else "No files found.")

        for i, f in enumerate(items, 1):
            print(f"{i}. {f['name']} (ID: {f['id']})")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
