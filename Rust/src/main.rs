#![allow(non_snake_case)]
use eframe::egui::{CentralPanel, Context, RichText};
use serde;

fn main() {
    let native_options = eframe::NativeOptions::default();
    let _ = eframe::run_native(
        "My egui App",
        native_options,
        Box::new(|cc| Box::new(UtilApp::new(cc))),
    );
}

#[derive(Default, serde::Deserialize, serde::Serialize)]
#[serde(default)]
struct UtilApp {
    prevC: String,
    prevY: String,
    prevF: String,
}

impl UtilApp {
    fn new(cc: &eframe::CreationContext<'_>) -> Self {
        // Customize egui here with cc.egui_ctx.set_fonts and cc.egui_ctx.set_visuals.
        // Restore app state using cc.storage (requires the "persistence" feature).
        // Use the cc.gl (a glow::Context) to create graphics shaders and buffers that you can use
        // for e.g. egui::PaintCallback.
        if let Some(storage) = cc.storage {
            let prevC = storage.get_string("prevC").unwrap_or_default();
            let prevF = storage.get_string("prevF").unwrap_or_default();
            let prevY = storage.get_string("prevY").unwrap_or_default();
            Self {
                prevC: prevC.parse().unwrap_or_default(),
                prevF: prevF.parse().unwrap_or_default(),
                prevY: prevY.parse().unwrap_or_default(),
            }
        } else {
            Self::default()
        }
    }
}

impl eframe::App for UtilApp {
    fn update(&mut self, ctx: &Context, frame: &mut eframe::Frame) {
        CentralPanel::default().show(ctx, |ui| {
            ui.heading("Fahrenheit to Celsius");
            ui.text_edit_singleline(&mut self.prevF);
            ui.label(
                RichText::new(format!(
                    "{}°C in Fahrenheit: {}°F",
                    self.prevF,
                    (self.prevF.parse::<f32>().unwrap_or_default() - 32.0) * 5.0 / 9.0
                ))
                .size(15.0),
            );

            ui.heading("Celsius to Fahrenheit");
            ui.text_edit_singleline(&mut self.prevC);
            ui.label(
                RichText::new(format!(
                    "{}°F in Celsius: {}°C",
                    self.prevC,
                    self.prevC.parse::<f32>().unwrap_or_default() * 9.0 / 5.0 + 32.0
                ))
                .size(15.0),
            );

            ui.heading("Leap Year Detector");
            ui.text_edit_singleline(&mut self.prevY);
            ui.label(
                RichText::new(format!(
                    "{} is {} a leap year",
                    self.prevY,
                    if self.prevY.parse::<i32>().unwrap_or_default() % 4 == 0 {
                        "is"
                    } else {
                        "is not"
                    }
                ))
                .size(15.0),
            );
        });
    }

    fn save(&mut self, storage: &mut dyn eframe::Storage) {
        storage.set_string("prevC", self.prevC.to_owned());
        storage.set_string("prevF", self.prevF.to_owned());
        storage.set_string("prevY", self.prevY.to_owned());
        storage.flush();
    }
}
