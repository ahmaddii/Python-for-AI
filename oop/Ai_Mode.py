class BaseModel:

    def __init__(self, model_name):
        self.model_name = model_name
        self.is_loaded = False

    def loaded(self):
        print(f"{self.model_name} is Loading ......")
        self.is_loaded = True


class TextModel(BaseModel):

    def __init__(self, model_name, max_length=1000):
        super().__init__(model_name)
        self.max_length = max_length

    def processText(self, text):
        if not self.is_loaded:
            self.loaded()
        if len(text) > self.max_length:
            text = text[:self.max_length]
        return f"Processed: {text}"


model = TextModel(model_name="gpt : 5 -3.5 turbo", max_length=100)

result = model.processText(text="Hello World")

print(result)
