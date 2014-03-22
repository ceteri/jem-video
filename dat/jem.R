# linear equation example

x = 1:10
y = 3 * x + 2
plot(x, y, type="o", main="y = 3x + 2")
grid()

# polynomial example

x = 1:10
y = 3 * x**2 + x - 5
plot(x, y, type="o", main="y = f(x)")
grid()

# system of equations

t = 1:30
d = 23*(t-10)
d1 = 11*(t-2)

plot(t, d, type="l", col="red")
lines(t, d1, type="l", col="blue")
abline(v=17.33, col="gray")

# latency graph

N = 100000
x = 1:N
y1 = x - 1
y2 = log(x)/log(2)
plot(x, y1, type="l", ylab="latency", xlab="scale", log="xy", col="red")
lines(x, y2, type="l", col="blue")
legend(2, N * .95, # placement 
       c("Ye Olde School", "Monoids, FTW"), # labels 
       lty=c(1,1), # symbols (lines)
       lwd=c(2.5,2.5),
       col=c("red","blue"), # color
       cex=0.75
)


# least squares approximation example

x <- c(0, 1, 2, 3)
y <- c(-1, 0.2, 0.9, 2.1)
df <- data.frame(x, y)

m <- lm(df$y ~ df$x)

plot(df, ylab="ratings", xlab="month")
abline(m, col="red")

# PCA example

d <- read.delim("/Users/ceteri/src/book/jem-book/dat/pca.tsv", 
                header=TRUE, sep="\t")
tendr <- c("carol","deepali","kirill")
d$tendr <- factor(d$tendr, tendr)
head(d)
round(cor(d[,1:4]), 2)

pc <- princomp(d[,1:4], cor=TRUE, scores=TRUE)
summary(pc)

plot(pc,type="lines")

plot(pc$scores[,1:2], col=d$tendr)
legend(0, 2.4, # placement 
       tendr, # labels 
       lty=c(1,1,1), # symbols
       lwd=c(1,1,1),
       col=c(1,2,3), # color
       cex=.77
)

#t(d)
