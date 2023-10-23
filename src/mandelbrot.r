run <- function(xmin, xmax, ymin, ymax, width, height, maxiter) {
  x <- seq(xmin, xmax, length.out = width)
  y <- seq(ymin, ymax, length.out = height)
  c <- outer(x, y, FUN = function(x, y) complex(real = x, imaginary = y))
  z <- c
  divtime <- matrix(maxiter, nrow = height, ncol = width)
  
  for (i in 1:maxiter) {
    z <- z^2 + c
    diverge <- Mod(z) > 2
    div_now <- diverge & (divtime == maxiter)
    divtime[div_now] <- i
    z[diverge] <- 2
  }
  
  return(t(divtime))
}

# Main function to parse command line arguments and run the simulation
main <- function() {
  args <- commandArgs(trailingOnly = TRUE)
  xmin <- as.numeric(args[1])
  xmax <- as.numeric(args[2])
  ymin <- as.numeric(args[3])
  ymax <- as.numeric(args[4])
  width <- as.integer(args[5])
  height <- as.integer(args[6])
  maxiter <- as.integer(args[7])
  
  result <- run(xmin, xmax, ymin, ymax, width, height, maxiter)
  print(result)
}

# Run the main function
main()