% Exemplo para o curso de SEL0417 - Fundamentos de Controle

% Simulação não linear - resposta a um degrau unitário

u = 0.1 ; 
k1 = 1 ;
k2 = 1 ;
k3 = 1 ; 
opcoes = [];
intervalo = [ 0 12 ] ; 
x0 = [ 0 0 ] ; 
[t,x] = ode45('xponto',intervalo,x0,opcoes,u,k1,k2,k3) ;

figure(1)
plot(t,x(:,1)) ; 

figure(2)
plot(t,x(:,2)) ; 

figure(3)
plot(x(:,1),x(:,2)) ;

