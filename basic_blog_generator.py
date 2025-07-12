def generate_blog(topic, keywords):
    intro = f"Today, let's explore the topic of {topic}. "
    body = f"This topic involves {', '.join(keywords)}. "
    end = "Hope this gave you insights into the subject."

    blog = intro + "\n\n" + body + "\n\n" + end
    return blog

# Command line
topic = input("Enter blog topic: ")
keywords = input("Enter keywords (comma separated): ").split(',')

blog_post = generate_blog(topic, keywords)
print("\nGenerated Blog:\n", blog_post)
