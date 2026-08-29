/* Copyright 2026 Tuan Phong
 * SPDX-License-Identifier: GPL-2.0-or-later
 */

#include QMK_KEYBOARD_H

enum layer_names {
    _BASE,
    _FN,
};

enum custom_keycodes {
    // Toggles between full RGB lighting and an indicators-only mode where
    // effects are dark but the Caps Lock and Fn indicators still render.
    PN_RGB_TOGG = SAFE_RANGE,
};

#define MAC_SPOTLIGHT LGUI(KC_SPC)
#define MAC_EMOJI LCG(KC_SPC)

// clang-format off
const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [_BASE] = LAYOUT(
        KC_ESC,  KC_F1,   KC_F2,   KC_F3,   KC_F4,   KC_F5,   KC_F6,   KC_F7,   KC_F8,   KC_F9,   KC_F10,  KC_F11,  KC_F12,  KC_MPLY,          KC_MUTE,
        KC_GRV,  KC_1,    KC_2,    KC_3,    KC_4,    KC_5,    KC_6,    KC_7,    KC_8,    KC_9,    KC_0,    KC_MINS, KC_EQL,  KC_BSPC,          KC_DEL,
        KC_TAB,  KC_Q,    KC_W,    KC_E,    KC_R,    KC_T,    KC_Y,    KC_U,    KC_I,    KC_O,    KC_P,    KC_LBRC, KC_RBRC, KC_BSLS,          KC_PGUP,
        KC_CAPS, KC_A,    KC_S,    KC_D,    KC_F,    KC_G,    KC_H,    KC_J,    KC_K,    KC_L,    KC_SCLN, KC_QUOT,          KC_ENT,           KC_PGDN,
        KC_LSFT,          KC_Z,    KC_X,    KC_C,    KC_V,    KC_B,    KC_N,    KC_M,    KC_COMM, KC_DOT,  KC_SLSH,          KC_RSFT, KC_UP,   KC_END,
        KC_LCTL, KC_LOPT, KC_LCMD,                            KC_SPC,                             KC_RCMD, KC_ROPT, MO(_FN),  KC_LEFT, KC_DOWN, KC_RGHT
    ),

    [_FN] = LAYOUT(
        PN_RGB_TOGG, KC_BRID, KC_BRIU, KC_MCTL, MAC_SPOTLIGHT, RM_VALD, RM_VALU, KC_MPRV, KC_MPLY, KC_MNXT, KC_MUTE, KC_VOLD, KC_VOLU, _______,    _______,
        _______, _______, _______, _______, _______,       _______, _______, _______, _______, _______, _______, _______, _______, _______,        _______,
        _______, RM_VALD, RM_VALU, _______, _______,       _______, _______, _______, _______, _______, _______, _______, _______, QK_BOOT,         RM_SPDU,
        _______, RM_SATD, RM_SATU, _______, _______,       _______, _______, _______, _______, _______, _______, _______,          _______,         RM_SPDD,
        _______,          RM_HUED, RM_HUEU, _______,       _______, _______, NK_TOGG, _______, _______, _______, _______,          _______, RM_NEXT, _______,
        _______, _______, _______,                                  MAC_EMOJI,                         _______, _______, _______, KC_HOME, RM_PREV, KC_END
    ),
};
// clang-format on

#if defined(ENCODER_MAP_ENABLE)
const uint16_t PROGMEM encoder_map[][NUM_ENCODERS][NUM_DIRECTIONS] = {
    [_BASE] = {ENCODER_CCW_CW(KC_VOLD, KC_VOLU)},
    [_FN]   = {ENCODER_CCW_CW(RM_VALD, RM_VALU)},
};
#endif

bool process_record_user(uint16_t keycode, keyrecord_t *record) {
    switch (keycode) {
        case PN_RGB_TOGG:
            if (record->event.pressed) {
                if (rgb_matrix_get_flags() == LED_FLAG_ALL) {
                    rgb_matrix_set_flags(LED_FLAG_NONE);
                } else {
                    rgb_matrix_set_flags(LED_FLAG_ALL);
                }
            }
            return false;
    }
    return true;
}

// LED index of the Caps Lock key in the GMMK Pro rev1 ANSI RGB matrix.
#define CAPS_LOCK_LED_INDEX 3

bool rgb_matrix_indicators_advanced_user(uint8_t led_min, uint8_t led_max) {
    // In indicators-only mode the effects skip every LED, so black them out
    // each frame before drawing the indicators on top.
    if (rgb_matrix_get_flags() == LED_FLAG_NONE) {
        for (uint8_t index = led_min; index < led_max; index++) {
            rgb_matrix_set_color(index, 0, 0, 0);
        }
    }

    if (get_highest_layer(layer_state) == _FN) {
        for (uint8_t row = 0; row < MATRIX_ROWS; row++) {
            for (uint8_t col = 0; col < MATRIX_COLS; col++) {
                uint8_t index = g_led_config.matrix_co[row][col];
                if (index == NO_LED || index < led_min || index >= led_max) {
                    continue;
                }
                uint16_t keycode = keymap_key_to_keycode(_FN, (keypos_t){col, row});
                if (keycode > KC_TRNS) {
                    RGB_MATRIX_INDICATOR_SET_COLOR(index, 255, 255, 255);
                }
            }
        }
    }

    if (host_keyboard_led_state().caps_lock) {
        RGB_MATRIX_INDICATOR_SET_COLOR(CAPS_LOCK_LED_INDEX, 255, 0, 0);
        for (uint8_t index = led_min; index < led_max; index++) {
            if (g_led_config.flags[index] & LED_FLAG_UNDERGLOW) {
                RGB_MATRIX_INDICATOR_SET_COLOR(index, 255, 0, 0);
            }
        }
    }

    return false;
}
