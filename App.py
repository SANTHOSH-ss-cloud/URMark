import streamlit as st

st.set_page_config(page_title="Internal Marks Calculator", page_icon="🧮")

st.title("🎓 Internal Marks Calculator (Out of 40)")
st.write("Calculate internal marks for multiple subjects with automatic CAT conversion and pass prediction.")

# Function to convert marks
def convert_marks(cat1, cat2, cat3, assignment):
    cat1_conv = (cat1 / 50) * 12
    cat2_conv = (cat2 / 25) * 6
    cat3_conv = (cat3 / 50) * 12
    assign_conv = (assignment / 10) * 10  # stays same
    total = cat1_conv + cat2_conv + cat3_conv + assign_conv
    return cat1_conv, cat2_conv, cat3_conv, assign_conv, total

# Number of subjects
num_subjects = st.number_input("Enter number of subjects", min_value=1, max_value=10, step=1)

results = []

for i in range(num_subjects):
    st.subheader(f"📘 Subject {i+1}")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        cat1 = st.number_input(f"CAT 1 Marks (out of 50)", min_value=0.0, max_value=50.0, key=f"cat1_{i}")
    with col2:
        cat2 = st.number_input(f"CAT 2 Marks (out of 25)", min_value=0.0, max_value=25.0, key=f"cat2_{i}")
    with col3:
        cat3 = st.number_input(f"CAT 3 Marks (out of 50)", min_value=0.0, max_value=50.0, key=f"cat3_{i}")
    with col4:
        assignment = st.number_input(f"Assignment (out of 10)", min_value=0.0, max_value=10.0, key=f"assign_{i}")

    cat1_conv, cat2_conv, cat3_conv, assign_conv, total = convert_marks(cat1, cat2, cat3, assignment)

    # Check pass/fail
    if total >= 24:
        status = f"✅ PASS (Total: {total:.2f} / 40)"
    else:
        needed = 24 - total
        # estimate needed improvement from CAT2 and CAT3 equally
        cat2_extra = needed / 2
        cat3_extra = needed / 2
        status = (
            f"❌ FAIL (Total: {total:.2f} / 40)\n"
            f"➡ You need +{cat2_extra:.2f} marks from CAT2 and +{cat3_extra:.2f} from CAT3 to pass."
        )

    st.write(f"**Result for Subject {i+1}:**")
    st.write(f"**Converted Marks:**")
    st.write(f"- CAT 1: {cat1_conv:.2f} / 12")
    st.write(f"- CAT 2: {cat2_conv:.2f} / 6")
    st.write(f"- CAT 3: {cat3_conv:.2f} / 12")
    st.write(f"- Assignment: {assign_conv:.2f} / 10")
    st.write(status)

    results.append({
        "Subject": f"Subject {i+1}",
        "Total (out of 40)": round(total, 2),
        "Status": "Pass" if total >= 24 else "Fail"
    })

st.divider()

# Summary Table
if results:
    st.subheader("📊 Summary of All Subjects")
    st.dataframe(results)

