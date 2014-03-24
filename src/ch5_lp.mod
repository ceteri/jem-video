/* foobartendr.io  ch5_lp.mod */

var x0 >= 0;
var x1 >= 0;
var x2 >= 0;

maximize
value: 5.0 * x0 + 3.0 * x1 + 2.0 * x2;

subject to

ingrednt:  1.0 * x0 + 1.0 * x1 + 3.0 * x2 <= 100;
bartendr: 10.0 * x0 + 4.0 * x1 + 5.0 * x2 <= 600;
delivery:  1.0 * x0 + 1.0 * x1 + 3.0 * x2 <= 150;

end;
