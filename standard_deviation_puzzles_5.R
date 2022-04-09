## Create sample of size 500 with mean of 45 and stdev of 10
sample <- rnorm(500, mean=45, sd=10)
## Add 10 points to each element
sample <- sample + 10
## Print stdev of the sample
print(sd(sample))
