; Tom Klootwijk Gambit 4.0 -- one_bit_not_sufficient
(set-option :produce-proofs true)
(set-option :timeout 15000)
(declare-const r1 Int)(declare-const r2 Int)(declare-const k Int)
(assert (and (<= 0 r1) (< r1 65536) (<= 0 r2) (< r2 65536) (= k 1)))
(assert (distinct (ite (>= (+ r1 k) 65536) 1 0) (ite (>= (+ r2 k) 65536) 1 0)))
(check-sat)
(get-model)
