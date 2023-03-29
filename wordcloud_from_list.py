import wordcloud
import matplotlib.pyplot as plt

def generate_word_map(terms):
    # Combine all terms into a single string
    text = ' '.join(terms)
    
    # Create a word cloud object with specified parameters
    wc = wordcloud.WordCloud(width=800, height=400, background_color='white').generate(text)
    
    # Display the word cloud image
    plt.figure(figsize=(12,6))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.show()

# Example usage
terms = ['apple', 'banana', 'cherry', 'date', 'elderberry']
generate_word_map(terms)
