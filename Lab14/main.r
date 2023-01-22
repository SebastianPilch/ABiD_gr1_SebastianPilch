library(magrittr)
library(datasets)
library(ggplot2)
library(GGally)
#list <- c(1, 3, 5, 2.5, .6, 3.1, 10, 4.2, 7, 2) 
list10 <- 1:10
print(list10)


list10 %<>% log2() %<>% sin() %<>% sum() %<>% sqrt()
print(list10)

data(iris)
agg <- iris %<>% aggregate(. ~ Species, .,mean)
print(agg)
data(iris)
irs_val <- ggplot(iris,aes(x = Sepal.Width)) + 
    geom_histogram(aes(fill=Species, color = Species), bins = 20)+
    geom_vline(data = agg, aes(xintercept = Sepal.Width, color=Species),
    linetype='dashed') + labs(x='x_axis',y='y_axis', title ='iris')

ggsave("rplot.jpg",plot = irs_val)

irs_val <- ggpairs(data=iris, aes(fill = Species, color = Species))
ggsave("pairplot.jpg",plot = irs_val)


x <- iris[,1:4]
y <- iris[,5]

sum_sqr <- c()
for(i in 1:10)
{
    kmeans_result <-kmeans(x,i)
    sum_sqr <- append(sum_sqr,kmeans_result$tot.withinss)
}


a <- ggplot(data.frame(iteration=1:length(sum_sqr), value = sum_sqr),aes(x=iteration, y=sum_sqr)) + geom_line()
ggsave("plot1_zad3.jpg", plot=a)


a <- ggplot(iris,aes(x=Sepal.Width, y=Petal.Width, color = kmeans_result$cluster)) +geom_point()
ggsave("plot2_zad3.jpg", plot=a)

a <- ggplot(iris, aes(x=Sepal.Width,y = Petal.Width, color=Species)) + geom_point()
ggsave("plot3_zad3.jpg", plot = a)