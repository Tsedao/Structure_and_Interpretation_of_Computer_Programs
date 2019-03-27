(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement.
(define (map fn lst)
  (define (map_helper fn lst result)
    (if (null? lst)
      result
      (map_helper fn (cdr lst) (cons (fn (car lst)) result))
    )
  )
  (reverse (map_helper fn lst '()))
)

(define (cons-all first rests)
  'replace-this-line)

(define (zip pairs)
  (if (null? pairs) '(() ())
    (cons (cons (car (car pairs)) (car (zip (cdr pairs)))) (cons (cons (car (cdr (car pairs))) (car (cdr (zip (cdr pair))))) nil))
  )
)
(define (zip pairs)
  (list (map car pairs) (map cadr pairs))
)

(define (reverse lst)
  (define (reverse_helper lst r)
    (if (null? lst)
      r
      (reverse_helper (cdr lst) (cons (car lst) r)
      )
    )
  )
  (reverse_helper lst '())
)

;; Problem 17
;; Returns a list of two-element lists
(define (enumerate s)
  (define (enumerate_helper s result num)
    (if (null? s)
      result
      (enumerate_helper (cdr s) (cons (cons num (cons (car s) nil)) result) (+ num 1))
    )
  )
  (reverse (enumerate_helper s '() 0))
)
  ; END PROBLEM 17

;; Problem 18

(define (map fn lst)
  (define (map_helper fn lst result)
    (if (null? lst)
      result
      (map_helper fn (cdr lst) (cons (fn (car lst)) result))
    )
  )
  (reverse (map_helper fn lst '()))
)



;; List all ways to make change for TOTAL with DENOMS

(define (list-change total denoms)
  (cond
    ((= total 0) '(()))
    ((or (< total 0) (null? denoms)) '())
    ((< total (car denoms)) (list-change total (cdr denoms)))
    (else (append
        (map (lambda (lst) (cons (car denoms) lst)) (list-change (- total (car denoms)) denoms))
        (list-change total (cdr denoms))
      )
    )
  )
)
  ; END PROBLEM 18

;; Problem 19
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 19
         expr
         ; END PROBLEM 19
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 19
         expr
         ; END PROBLEM 19
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           (cons form (cons params (let-to-lambda body)))
           ; END PROBLEM 19
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           (cons (cons 'lambda (cons (car (let-to-lambda (zip values))) (let-to-lambda body))) (cadr (let-to-lambda (zip values))))
           ; END PROBLEM 19
           ))
        (else
         ; BEGIN PROBLEM 19
         (map let-to-lambda expr)
         ; END PROBLEM 19
         )))
