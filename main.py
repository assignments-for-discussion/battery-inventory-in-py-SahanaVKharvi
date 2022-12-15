
def count_batteries_by_usage(cycles):
  return {
    "lowCount": 0,
    "mediumCount": 0,
    "highCount": 0
for i in range (cycles):
    if "lowCount" < 310:
         print("low")
    elif "mediumCount" < 310 and "mediumCount" > 929:
         print("medium")
    elif "highCount" > 929:
         print("high")
    else:
         print("nothing")
  }




def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
