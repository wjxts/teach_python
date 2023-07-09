s1 = "monday"
s2 = "sunday"
#print(s1, s2)
# ----------------------
# goal: upperize the first character of s1 and last character of s2, then concatenate them with "+". print the result
s1 = s1[0].upper() + s1[1:]
s2 = s2[:-1] + s2[-1].upper()
s3 = f"{s1}+{s2}"
s4 = "+".join([s1, s2])
print(s3, s4, sep="\n")
