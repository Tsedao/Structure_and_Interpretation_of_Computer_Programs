; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)

(define (sign x)
  (cond
    ((< x 0) -1)
    ((> x 0) 1)
    (else 0)
  )
)

(define (ordered? s)
  (cond
    ((null? (cdr s)) #t)
    ((> (car s) (car (cdr s))) #f)
    (else (ordered? (cdr s)))
  )
)

(define (nodots s)
  (cond
    ((null? s) s)
    ((not (pair? s)) (cons s nil))
    ((not (pair? (car s))) (cons (car s) (nodots (cdr s))))
    (else (cons (nodots (car s)) (nodots (cdr s))))
  )
)



; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
    (cond ((empty? s) false)
          ((> (car s) v) false)
          ((= (car s) v) true)
          (else (contains? (cdr s) v))
          ))

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return s is Link.empty
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

(define (add s v)
    (cond ((empty? s) (list v))
          ((> (car s) v) (cons v s))
          ((= (car s) v) s)
          (else (cons (car s) (add (cdr s) v)))
          ))

(define (intersect s t)
    (cond ((or (empty? s) (empty? t)) nil)
          (else
           (cond
              ((= (car s) (car t)) (cons (car s) (intersect (cdr s) (cdr t))))
              ((< (car s) (car t)) (intersect (cdr s) t))
              (else  (intersect s (cdr t)))
            )
          )))

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
    (cond ((empty? s) t)
          ((empty? t) s)
          ((= (car s) (car t)) (cons (car s) (union (cdr s) (cdr t))))
          ((> (car s) (car t)) (union t s))
          (else (cons (car s) (union (cdr s) t)))
          ))

; Tail-Calls in Scheme

(define (exp-recursive b n)
  (if (= n 0)
      1
      (* b (exp-recursive b (- n 1)))))

(define (exp b n)
  ;; Computes b^n.
  ;; b is any number, n must be a non-negative integer.
  (define (exp_tail b n result)
    (if (= n 0)
      result
      (exp_tail b (- n 1) (* b result))
    )
  )
  (exp_tail b n 1)
)

(define (filter pred lst)
  (define (filter-tail pred lst result)
    (cond
      ((null? lst) result)
      ((pred (car lst)) (filter-tail pred (cdr lst) (append result (list (car lst)))))
      (else (filter-tail pred (cdr lst) result))
    )
  )
  (filter-tail pred lst nil)
)
