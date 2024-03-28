n = int(input())

gold = 0
silver = 0
bronze = 0
gold_count = 0
silver_count = 0
bronze_count = 0

for _ in range(n):
    score = int(input())
    if score == gold:
        gold_count += 1
    elif score == silver:
        silver_count += 1
    elif score == bronze:
        bronze_count += 1
    elif score > gold:
        bronze = silver
        bronze_count = silver_count
        silver = gold
        silver_count = gold_count
        gold = score
        gold_count = 1
    elif score > silver:
        bronze = silver
        bronze_count = silver_count
        silver = score
        silver_count = 1
    elif score > bronze:
        bronze = score
        bronze_count = 1

print(bronze, bronze_count)
