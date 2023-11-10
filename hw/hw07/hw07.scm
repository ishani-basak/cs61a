(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr (cdr s))))

(define (ordered? s) (if (null? (cdr s)) 
                        #t 
                        (if (> (car s) (cadr s))
                            #f
                            (ordered? (cdr s))
                        )
                    ))

(define (square x) (* x x))

(define (pow base exp)  
    (if (or (= base 1) (= exp 0))
        1
        (if (= exp 2)
            (square base)
            (if (= (modulo exp 2) 0)
                (square (pow base (/ exp 2)))
                (* base (square (pow base (quotient exp 2))))
            )
        )
    )
)