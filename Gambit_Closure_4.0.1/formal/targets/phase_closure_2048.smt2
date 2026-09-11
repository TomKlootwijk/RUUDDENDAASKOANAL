; Tom Klootwijk Gambit 4.0 -- phase_closure_2048
(set-option :produce-proofs true)
(set-option :timeout 15000)
(declare-const a Int)(declare-const s Int)(assert (and (<= 0 a) (< a 2048) (<= 0 s) (< s 2048)))
(define-fun next () Int (mod (+ a s) 2048))
(assert (not (and (<= 0 next) (< next 2048))))
(check-sat)
(get-proof)
