import uuid

def generate_id() -> str:
   parts = str(uuid.uuid4()).split("-")
   return f"{parts[0]} - {parts[1]}{parts[2]}"

# print(generate_id()) # 2e491d2b - 8e7c - 42f5