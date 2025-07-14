import praw
import time

# ✅ Reddit API credentials (demo values)
reddit = praw.Reddit(
    client_id="4U_Mhpl0WWDV4cbfgCoqmw",
    client_secret="1Z6W5xANHd2R1IeP6u6a0DQi5A-_dw",
    user_agent="user-persona-script by u/Far_Living8259"
)

# 🔹 Reddit username input
url = input("Enter Reddit profile URL (like https://www.reddit.com/user/example/): ").strip()
username = url.rstrip("/").split("/")[-1]

# 🔍 Get Redditor object
try:
    redditor = reddit.redditor(username)
    _ = redditor.id  # test fetch
except Exception as e:
    print("User not found or not accessible. Try another username.")
    exit()

# 📥 Fetch posts and comments
posts = []
comments = []

print("Getting recent posts...")
for post in redditor.submissions.new(limit=20):
    posts.append(f"Title: {post.title}\nBody: {post.selftext}\nSubreddit: {post.subreddit}\nLink: {post.url}\n")
    time.sleep(0.2)

print("Getting recent comments...")
for comment in redditor.comments.new(limit=20):
    comments.append(f"Comment: {comment.body}\nSubreddit: {comment.subreddit}\nLink: https://reddit.com{comment.permalink}\n")
    time.sleep(0.2)

# 💾 Save raw data
with open(f"{username}_data.txt", "w", encoding="utf-8") as f:
    f.write("=== POSTS ===\n\n")
    for p in posts:
        f.write(p + "\n")
    f.write("=== COMMENTS ===\n\n")
    for c in comments:
        f.write(c + "\n")

print("Finished saving data.")

# 🔍 NOTE:
# This script currently only fetches and stores the Reddit user’s posts and comments.
# GPT-based persona generation is NOT integrated here due to limited API credits.
# 
# 🔮 If OpenAI API credits are available, the following improvements can be done:
# 1. Automatically send the scraped data to GPT (via openai.ChatCompletion.create)
# 2. Generate a user persona based on writing style, interest, tone, etc.
# 3. Save the GPT output as <username>_persona_output.txt
#
# This will make the entire process fully automated.
# For now, the persona is created manually using GPT and attached as a separate file.

print(f"⚠️ GPT API call skipped. Please refer to '{username}_persona_output.txt' for the final user persona.")
