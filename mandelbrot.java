import java.util.ArrayList;

class Complex {
    public double x, y;

    public Complex(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public Complex add(Complex other) {
        return new Complex(this.x + other.x, this.y + other.y);
    }

    public Complex mul(Complex other) {
        return new Complex(
                this.x * this.x - this.y * other.y,
                this.x * other.y + this.y * other.x
        );
    }

    public double abs() {
        return Math.abs(this.x * this.x - this.y * this.y);
    }
}

public class mandelbrot {
    public static ArrayList<Double> linspace(double vmin, double vmax, int length) {
        double step = (vmax - vmin) / (length - 1);
        ArrayList<Double> ret = new ArrayList<Double>();
        int i = 0;
        double v = vmin;
        for (; i < length; i++) {
            ret.add(v);
            v += step;
        }
        return ret;
    }

    public static ArrayList<Complex> participants(ArrayList<Double> X, ArrayList<Double> Y) {
        ArrayList<Complex> ret = new ArrayList<Complex>();
        for (double y : Y) {
            for (double x: X) {
                ret.add(new Complex(x, y));
            }
        }
        return ret;
    }

    public static ArrayList<Integer> calc(ArrayList<Complex> C, int maxiter, int threshold) {
        ArrayList<Integer> ret = new ArrayList<Integer>();
        for (Complex c: C) {
            Complex z = new Complex(0, 0);
            int i = 0;
            for (; i < maxiter; i++) {
                z = z.mul(z).add(c);
                if (z.abs() > threshold) {
                    break;
                }
            }
            ret.add(i);
        }
        return ret;
    }

    public static ArrayList<Integer> run(double xmin, double xmax, double ymin, double ymax, int width, int height, int maxiter) {
        ArrayList<Double> X = linspace(xmin, xmax, width);
        ArrayList<Double> Y = linspace(ymin, ymax, height);
        ArrayList<Complex> C = participants(X, Y);
        ArrayList<Integer> steps = calc(C, maxiter, 4);
        return steps;
    }

    public static void main(String args[]) {
        double xmin = Double.parseDouble(args[0]);
        double xmax = Double.parseDouble(args[1]);
        double ymin = Double.parseDouble(args[2]);
        double ymax = Double.parseDouble(args[3]);
        int width = Integer.parseInt(args[4]);
        int height = Integer.parseInt(args[5]);
        int maxiter = Integer.parseInt(args[6]);

        run(xmin, xmax, ymin, ymax, width, height, maxiter);
    }
}
