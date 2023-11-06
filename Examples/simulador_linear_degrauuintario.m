% Exemplo para o curso de SEL0417 - Fundamentos de Controle

% Simulação linear - resposta a um degrau unitário

A = [ 0 1 ; -1 -1 ] ; 
B = [ 0 ; 0.1 ] ; 
C = [ 1 0 ] ; 
D = 0 ; 

[y,x,t] = step(A,B,C,D) ; 

figure(1)
plot(t,y) ;

figure(2)
plot(t,x(:,2)) ;

figure(3)
plot(x(:,1),x(:,2)) ;

