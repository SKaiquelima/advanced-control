% Exemplo para o curso de SEL0417 - Fundamentos de Controle

% Função não linear

function xponto = odefile(t,x,opcoes,u,k1,k2,k3)

xponto(1,1) = x(2) ; 
xponto(2,1) = -k1*sin(x(1))-k2*x(2)+k3*u ;

