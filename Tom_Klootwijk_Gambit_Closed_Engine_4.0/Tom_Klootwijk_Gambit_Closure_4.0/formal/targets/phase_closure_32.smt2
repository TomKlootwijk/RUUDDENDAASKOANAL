; Tom Klootwijk Gambit 4.0 -- phase_closure_32
(set-option :produce-proofs true)
(set-option :timeout 15000)
(declare-const a Int)(declare-const s Int)(assert (and (<= 0 a) (< a 32) (<= 0 s) (< s 32)))
(define-fun next () Int (mod (+ a s) 32))
(assert (not (and (<= 0 next) (< next 32))))
(check-sat)
(get-proof)
