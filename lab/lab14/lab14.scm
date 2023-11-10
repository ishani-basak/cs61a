(define (split-at lst n)
    (cond 
        ((= n 0) (cons nil lst))
        ((null? lst) (cons nil nil))
        (else 
            (cons 
                (cons (car lst) (car (split-at (cdr lst) (- n 1))))
                (cdr (split-at (cdr lst) (- n 1)))
            )
        )
    )
)

(define (compose-all funcs)
    (define (do-funcs fs x) 
        (if (null? fs) 
            x 
            (let ((x ((car fs) x)))
                (do-funcs (cdr fs) x)
            )        
        )
    )
    (lambda (x) (do-funcs funcs x))
)


    