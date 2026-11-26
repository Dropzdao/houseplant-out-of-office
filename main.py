def validate(text):
    assert len(text) <= 200, "entry line too long"
    assert text.strip(), "entry line must not be blank"


line = "Out of office: last watered in March. I now run on sunlight, spite, and the hope someone reads this."

validate(line)
print(line)
