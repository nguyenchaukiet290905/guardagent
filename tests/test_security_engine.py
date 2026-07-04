from app.security_engine import detect_leakage

tests = [
    "",
    "Hello world",
    "sk-123",
    "sk-abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGH1234"
]

for text in tests:
    print("=" * 50)
    print("Testing:", text)
    detect_leakage(text)

