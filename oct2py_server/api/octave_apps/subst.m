function [out] = subst(x, y)
    out = x - square(y);

function [out] = square(x)
	out = x * x