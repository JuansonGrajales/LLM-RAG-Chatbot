from pydantic import BaseModel

# used to verify that the POST request body includes a text field with a string value.
class HospitalQueryInput(BaseModel):
    text: str
# verifies that the response body sent back includes input, output, and intermediate_steps.
class HospitalQueryOutput(BaseModel):
    input: str
    output: str
    intermediate_steps: list[str]
