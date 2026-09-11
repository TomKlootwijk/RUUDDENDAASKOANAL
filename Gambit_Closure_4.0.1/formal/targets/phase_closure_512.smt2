; Tom Klootwijk Gambit 4.0 -- phase_closure_512
(set-option :produce-proofs true)
(set-option :timeout 15000)
(declare-const a Int)(declare-const s Int)(assert (and (<= 0 a) (< a 512) (<= 0 s) (< s 512)))
(define-fun next () Int (mod (+ a s) 512))
(assert (not (and (<= 0 next) (< next 512))))
(check-sat)
(get-proof)
