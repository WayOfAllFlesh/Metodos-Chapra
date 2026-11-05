fprintf("Entre com os coeficientes: ");
a = input("Entre com o A: ");
b = input("Entre com o B: ");
c = input("Entre com o C: ");

[x1, x2, condition] = raiz2grau(a, b, c);

if condition == 0
    fprintf("As raizes da equação são: %f | %f", x1, x2);
elseif condition == 1
    fprintf("As raiz da equação é: %f", x1);
else
    fprintf("As raizes da equação são: %f +- %f i", x1, x2);
end

function [x1, x2, condition] = raiz2grau(a, b, c)
    delta = b^2 - 4*a*c;
    if delta > 0
        x1 = -b/(2*a) + (delta)^(1/2)/(2*a);
        x2 = -b/(2*a) - (delta)^(1/2)/(2*a);
        condition = 0;
    elseif delta == 0
        x1 = -b/(2*a);
        x2 = 0;
        condition = 1;
    else
        x1 = -b/(2*a);
        x2 = (-delta)^(1/2)/(2*a);
        condition = 3;
    end
end

