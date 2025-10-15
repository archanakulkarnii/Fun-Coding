import streamlit as st

st.title("🧠 Fun Python & General Knowledge Quiz")

# --- Questions ---
q1 = st.radio("1️⃣ Which planet in our solar system has the most moons?",
              ["Earth", "Jupiter", "Saturn", "Mars"])
q2 = st.radio("2️⃣ What programming language is known as the 'language of the web'?",
              ["Python", "C++", "JavaScript", "Java"])
q3 = st.radio("3️⃣ Which data structure works on the principle of LIFO (Last In, First Out)?",
              ["Queue", "Stack", "List", "Array"])
q4 = st.radio("4️⃣ What is the fastest land animal?",
              ["Lion", "Cheetah", "Tiger", "Horse"])
q5 = st.radio("5️⃣ Which fruit is known as the 'king of fruits'?",
              ["Apple", "Mango", "Banana", "Orange"])
q6 = st.radio("6️⃣ What is the smallest prime number?",
              ["1", "2", "3", "5"])
q7 = st.radio("7️⃣ Which metal is liquid at room temperature?",
              ["Mercury", "Silver", "Gold", "Copper"])
q8 = st.radio("8️⃣ Which ocean is the largest in the world?",
              ["Indian", "Atlantic", "Pacific", "Arctic"])
q9 = st.radio("9️⃣ What is the national flower of Japan?",
              ["Rose", "Lotus", "Cherry Blossom", "Tulip"])
q10 = st.radio("🔟 Which planet is known as the Red Planet?",
               ["Earth", "Mars", "Venus", "Jupiter"])

# --- Check score ---
score = 0
if st.button("✅ Check Score"):
    if q1 == "Saturn":
        score += 1
    if q2 == "JavaScript":
        score += 1
    if q3 == "Stack":
        score += 1
    if q4 == "Cheetah":
        score += 1
    if q5 == "Mango":
        score += 1
    if q6 == "2":
        score += 1
    if q7 == "Mercury":
        score += 1
    if q8 == "Pacific":
        score += 1
    if q9 == "Cherry Blossom":
        score += 1
    if q10 == "Mars":
        score += 1

    st.session_state["score"] = score
    st.session_state["checked"] = True

    st.success(f"🎯 Your Score: {score}/10")

    if score == 10:
        st.balloons()
        st.info("Excellent! 🌟 You got all correct!")
    elif score >= 5:
        st.warning("Good job! 👍 Try again for a perfect score!")
    else:
        st.error("Keep practicing! 💪 You’ll get better next time!")

# --- Show Report ---
if st.session_state.get("checked", False):
    if st.button("📄 Show Report"):
        st.write("### Quiz Report:")

        # Question 1
        st.markdown(f"1️⃣ {q1} {'✅ Correct' if q1=='Saturn' else '❌ Wrong'}")
        # Question 2
        st.markdown(f"2️⃣ {q2} {'✅ Correct' if q2=='JavaScript' else '❌ Wrong'}")
        # Question 3
        st.markdown(f"3️⃣ {q3} {'✅ Correct' if q3=='Stack' else '❌ Wrong'}")
        # Question 4
        st.markdown(f"4️⃣ {q4} {'✅ Correct' if q4=='Cheetah' else '❌ Wrong'}")
        # Question 5
        st.markdown(f"5️⃣ {q5} {'✅ Correct' if q5=='Mango' else '❌ Wrong'}")
        # Question 6
        st.markdown(f"6️⃣ {q6} {'✅ Correct' if q6=='2' else '❌ Wrong'}")
        # Question 7
        st.markdown(f"7️⃣ {q7} {'✅ Correct' if q7=='Mercury' else '❌ Wrong'}")
        # Question 8
        st.markdown(f"8️⃣ {q8} {'✅ Correct' if q8=='Pacific' else '❌ Wrong'}")
        # Question 9
        st.markdown(f"9️⃣ {q9} {'✅ Correct' if q9=='Cherry Blossom' else '❌ Wrong'}")
        # Question 10
        st.markdown(f"🔟 {q10} {'✅ Correct' if q10=='Mars' else '❌ Wrong'}")
