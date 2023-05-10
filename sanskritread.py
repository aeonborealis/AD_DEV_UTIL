from sanskrit_data.schema import common
from sanskrit_data.parser.sandhi import Sandhi
from sanskrit_data.parser.util import ParserConfig
from sanskrit_data.parser.pratyaya import *
from sanskrit_data.parser.vocab import *
from sanskrit_data.parser.lexical_analyzer import LexicalAnalyzer
import re

# Define the Sanskrit text to be read
sanskrit_text = "असतो मा सद्गमय | तमसो मा ज्योतिर्गमय | मृत्योर्मा अमृतं गमय ||"

# Use the SanskritData library to tokenize and parse the text
config = ParserConfig()
analyzer = LexicalAnalyzer()
tokens = analyzer.tokenize(sanskrit_text, script=common.DEVANAGARI, replace_abbrev=False)
parsed_text = analyze_pratyaya(config, tokens)

# Use regular expressions to remove the tags from the parsed text
clean_text = re.sub('<.*?>', '', str(parsed_text))

# Print the clean text
print(clean_text)
