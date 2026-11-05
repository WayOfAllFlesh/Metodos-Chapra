tamanho_maximo = 1000;

valores = zeros(tamanho_maximo);
status = 0;
idx = 1;

while status ~= 1
    valor = input("Entre com o valor do cartão: ");
    status = input("Entre se é o cartão de saída (1 - Sim | 0 - Não): ");

    if status ~= 0 && status ~= 1
        while status ~= 0 && status ~= 1
            status = input("Entre se é o cartão de saída (1 - Sim | 0 - Não): ");
        end
    end

    valores(idx) = valor;
    idx = idx + 1;
end

somatorio = soma(valores, idx);
medians = media(valores, idx);
maxi = maximo(valores, idx);

fprintf("\nMax = %f | Media = %f | Soma = %f", maxi, medians, somatorio);

function soma = soma(valores, idx)
tamanho = idx - 1;

soma = 0;
for i = 1:tamanho
    soma = soma + valores(i);
end

end

function medians = media(valores, idx)
tamanho = idx - 1;

soma = 0;
for i = 1:tamanho
    soma = soma + valores(i);
end

medians = soma / tamanho;
end

function max = maximo(valores, idx)
tamanho = idx - 1;

maior = valores(1);
for i = 1:tamanho
    if valores(i) > maior
        maior = valores(i);
    end
end
max = maior;
end

