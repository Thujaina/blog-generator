# blog_generator.py

def generate_intro(topic):
    return f"Today, let's dive into the topic of {topic}. It's one of the most discussed subjects in the current era.\n"

def generate_body(keywords):
    body = "This topic is closely related to "
    body += ', '.join(keywords[:-1]) + f", and {keywords[-1]}.\n"
    body += "Each of these concepts plays a vital role in understanding the topic deeply.\n"
    return body

def generate_conclusion(topic):
    return f"To conclude, {topic} is an evolving area that offers endless opportunities for exploration and growth.\n"

def generate_blog(topic, keywords):
    blog = ""
    blog += generate_intro(topic)
    blog += "\n"
    blog += generate_body(keywords)
    blog += "\n"
    blog += generate_conclusion(topic)
    return blog

def save_to_file(content, filename="generated_blog.txt"):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    print("📝 Blog Generator\n---------------------")
    topic = input("Enter your blog topic: ").strip()
    keywords_input = input("Enter keywords (comma separated): ").strip()
    keywords = [kw.strip() for kw in keywords_input.split(',') if kw.strip()]

    if not topic or not keywords:
        print("❌ Invalid input. Please enter a topic and at least one keyword.")
        return

    blog = generate_blog(topic, keywords)

    print("\n✅ Generated Blog:\n")
    print(blog)

    save_to_file(blog)
    print("📁 Blog saved to 'generated_blog.txt'")

if __name__ == "__main__":
    main()
