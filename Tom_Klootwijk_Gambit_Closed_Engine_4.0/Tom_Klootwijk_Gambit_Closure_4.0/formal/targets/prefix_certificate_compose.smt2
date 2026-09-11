; Tom Klootwijk Gambit 4.0 -- prefix_certificate_compose
(set-option :produce-proofs true)
(set-option :timeout 15000)
(declare-const Q1 Int)(declare-const K1 Int)(declare-const Q2 Int)(declare-const K2 Int)(declare-const r0 Int)(declare-const r1 Int)(declare-const r2 Int)
(assert (= (+ (* 65536 Q1) r1) (+ r0 K1)))(assert (= (+ (* 65536 Q2) r2) (+ r1 K2)))
(assert (not (= (+ (* 65536 (+ Q1 Q2)) r2) (+ r0 K1 K2))))
(check-sat)
(get-proof)
