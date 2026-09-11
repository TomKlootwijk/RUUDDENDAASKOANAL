; Tom Klootwijk Gambit 4.0 -- hysteresis_total
(set-option :produce-proofs true)
(set-option :timeout 15000)
(declare-const f Int)(declare-const H Int)(declare-const old Bool)(assert (>= H 1))
(define-fun left () Bool (<= f (- H)))(define-fun right () Bool (>= f H))
(assert (and left right))
(check-sat)
(get-proof)
